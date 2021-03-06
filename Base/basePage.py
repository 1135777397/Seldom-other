"""
    author: kawi
    time: 22/03/08
    update:
    Notes:定义一个页面基类，让所有页面都继承这个类，封装常用的页面操作方法到这个类
          许多控件的操作方法
"""
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Common_Function.logger import Logger
from selenium.common.exceptions import ElementNotInteractableException, WebDriverException, \
    StaleElementReferenceException
# 暂时用这个ui，后续接jenkins
from Common_Function.HTMLTestReportCN import DirAndFiles
# inspect模块是针对模块，类，方法，功能等对象提供些有用的方法
import inspect
from selenium.webdriver.remote.webelement import WebElement
import time
from selenium.webdriver.common.keys import Keys

# create a logger instance
logger = Logger(logger="ElementOperation").getlogger()


class BasePage(object):
    """
        定义一个页面基类，让所有页面都继承这个类，封装常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver
        self.daf = DirAndFiles()

    # 只读属性
    @property
    def title(self):
        """获取当前网页的标题"""
        # 最多等待2秒
        max_times = 5
        for i in range(max_times):
            try:
                return self.driver.title
            except WebDriverException as e:
                if i < max_times - 1:
                    time.sleep(0.5)
                    print(1)
                else:
                    raise e

    @property
    def browser_name(self):
        """获取浏览器名称"""
        return self.driver.name

    @property
    def page_source(self):
        """获取页面所有元素"""
        return self.driver.page_source

    @property
    def current_window_handle(self):
        """获取当前窗口句柄"""
        return self.driver.current_window_handle

    @property
    def window_handles(self):
        """获取当前浏览器窗口句柄"""
        return self.driver.window_handles

    def switch_to_window(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_to_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    def switch_to_default_content(self):
        # 跳到最外层页面
        self.driver.switch_to.default_content()

    @property
    def get_text(self, element):
        """获取当前控件的text值"""
        logger.info("element's text is {}".format(self.driver.find_element(element).text))
        return self.driver.find_element(element).text

    @property
    def web_alert(self, action_type='accept'):
        """
        :action_type accept、dismiss
        :return:
        """
        if action_type:
            action_type.lower()
        alert = self.driver.switch_to.alert
        if action_type == 'accept':
            alert.accept()
        elif action_type == 'dismiss':
            alert.dismiss()

    @property
    def get_alert_text(self):
        """获取alert的信息"""
        alert = self.driver.switch_to.alert
        return alert.text

    @property
    def submit(self, element):
        """提交表单"""
        self.driver.find_element(element).submit()

    def select_dropDownBox_by_value(self, element, value):
        """
        适用单选下拉框
        :param element:
        :param values:
        :return:
        """
        logger.info(element, value)
        webElement = self.find_element(element)
        if webElement:
            webElement = Select(webElement)
            webElement.deselect_all()
            webElement.select_by_value(value)
            logger.error("未查到{0}".format(value))
        else:
            logger.error("传入的定位{0}有误".format(element))

    def is_displayed(self, element):
        """是否可见"""
        flag = self.driver.find_element(element).is_displayed()
        return flag

    def is_enabled(self, element):
        """元素是否可以进行操作"""
        webElement = self.find_element(element, displayed=True)
        flag = webElement.is_enabled()
        return flag

    def get(self, url):
        """打开一个新页面"""
        return self.driver.get(url)

    def refresh(self):
        """刷新当前页面"""
        logger.info("refresh page")
        return self.driver.refresh()

    def execute_script(self, script, *args):
        """执行js命令"""
        logger.info("Execute the JS command {} {}.".format(script, *args))
        return self.driver.execute_script(script, *args)

    def current_url(self):
        """获取当前url"""
        logger.info("get current url")
        return self.driver.current_url()

    def forward(self):
        """浏览器前进"""
        logger.info("Click forward on current page.")
        return self.driver.forward()

    def back(self):
        """浏览器后退"""
        logger.info("Click back on current page.")
        return self.driver.back()

    def close(self):
        """关闭当前窗口"""
        logger.info("Closing current window.")
        return self.driver.close()

    def set_window_size(self, width, height, windowHandle='current'):
        """设置窗口尺寸"""
        logger.info("set window size width{0}-height{1}".format(width, height))
        return self.driver.set_window_size(width, height, windowHandle)

    def get_window_size(self, windowHandle='current'):
        """获取窗口尺寸"""
        logger.info("get window size")
        return self.driver.get_window_size(windowHandle)

    def sleep(self, seconds):
        """
        程序休眠
        :param seconds: 等待时长（s）
        :return:
        """
        logger.info("Sleep for {} seconds".format(seconds))
        time.sleep(seconds)

    @property
    def get_current_function(self):
        """获取当前方法名称"""
        return inspect.stack()[1][3]

    def get_background_color(self, locate):
        """
        获取当前元素的背景颜色
        :param locate: 元素定位
        :return:
        """
        element = self.driver.find_element(*locate)
        return element.value_of_css_property("background-color")

    def get_table_data(self, locate, data_type='text'):
        """
        以二维数组返回表格每一行的每一列的数据[[row1][row2][colume1,clume2]]
        :param locate: 元素定位
        :param data_type: text-返回表格文本内容,html-返回表格html内容,webElement-返回表格元素
        :return:
        """
        webElement = self.find_element(locate, displayed=True)
        table_data = []
        table_trs = webElement.find_elements_by_tag_name('tr')
        try:
            # 为防止表格内的内容变化导致无法获取内容,进行异常捕获
            for tr in table_trs:
                tr_data = []
                tr_tds = tr.find_elements_by_tag_name('td')
                if data_type.lower() == 'text':
                    for td in tr_tds:
                        tr_data.append(td.text)
                elif data_type.lower() == 'html':
                    for td in tr_tds:
                        tr_data.append(td.get_attribute('innerHTML'))
                elif data_type.lower() == 'webelement':
                    tr_data = tr_tds
                table_data.append(tr_data)
        except StaleElementReferenceException as e:
            logger.error('获取表格内容异常:' + e.msg)
        return table_data

    def get_table_data_by_list(self, locate, list=1, data_type='text'):
        table_list = []
        table_data = self.get_table_data(locate, data_type=data_type)
        logger.info("获取表格第{}列数据".format(list))
        for i in range(0, len(table_data)):
            table_list.append(table_data[i][list - 1])
        return table_list

    def get_table_data_by_row(self, locate, row=1, data_type='text'):
        table_list = []
        table_data = self.get_table_data(locate, data_type=data_type)
        logger.info("获取表格第{}行数据".format(row))
        for i in range(0, len(table_data)):
            table_list.append(table_data[row - 1][i])
        return table_list

    def swipe(self, direction, length=None):
        """
        滑动窗口
        :param direction: 滑动方向，可以是up,down,left,right
        :param length: 滑动的长度，为默认值时滑动半屏
        :return:
        window.scrollBy({左右},{上下})
        """
        # 如果长度为默认值，则获取当前屏幕的长宽，设置滑动长度
        if length == None and direction == 'up' or direction == 'down':
            length = 0.5 * float(self.driver.get_window_size()['height'])
        elif length == None and direction == 'left' or direction == 'right':
            length = 0.5 * float(self.driver.get_window_size()['width'])

        if direction == 'up':
            logger.info('The screen scrolling up and the length is {}.'.format(length))
            self.driver.execute_script('window.scrollBy(0,{})'.format(length))
        elif direction == 'down':
            logger.info('The screen scrolling down and the length is {}.'.format(length))
            length = str(-1 * int(length))
            self.driver.execute_script('window.scrollBy(0,{})'.format(length))
        elif direction == 'left':
            logger.info('The screen scrolling left and the length is {}.'.format(length))
            self.driver.execute_script('window.scrollBy({},0)'.format(length))
        elif direction == 'right':
            logger.info('The screen scrolling right and the length is {}.'.format(length))
            length = str(-1 * int(length))
            self.driver.execute_script('window.scrollBy({},0)'.format(length))
        else:
            logger.error(
                'Entered the wrong direction "{}", please confirm whether it is one of up, down, left, right！'.format(
                    direction))
            raise WebDriverException(
                'Entered the wrong direction "{}", please confirm whether it is one of up, down, left, right！'.format(
                    direction))

    def find_element(self, locate, index=0, max_times=20, delay=0.5, displayed=True):
        """
        定位元素方法,用于定位多个属性相同的元素,当index为None时返回的是符合匹配规则的元素列表
        :param locate: 元素定位
        :param index: 序号，第一个为0，第二个为1，以此类推，默认为0，当为None时返回所有符合条件的元素
        :param max_times: 最大循环次数，默认为20次
        :param delay: 延时，默认为0.5秒
        :param displayed: 是否必须等待到元素可见才算找到元素，默认为是
        :return:
        """
        # 是否报错的标志
        error = False
        # 是否已定位到的标志
        flag = False
        for i in range(max_times):
            # 当前已定位到num个元素
            num = 0
            try:
                elements = self.driver.find_elements(*locate)
                if elements == None or elements == []:
                    if i < max_times - 1:
                        logger.info(
                            "The server doesn't send a response and the position will be retried after {} seconds!".format(
                                delay))
                    continue
                if index == None:
                    for element in elements:
                        if element.is_displayed() == False and displayed == True:
                            if i < max_times - 1:
                                logger.info(
                                    "The elements has been positioned but one of the elements is not visible and will be repositioned after {} seconds!".format(
                                        delay))
                            break
                        else:
                            num += 1
                    if num == len(elements):
                        flag = True
                        logger.info("Positioned the elements {}.".format(locate))
                        return elements
                else:
                    element = elements[index]
                    if element.is_displayed() == False and displayed == True:
                        logger.info(
                            "The element has been positioned but the element is not visible and will be repositioned after {} seconds!".format(
                                delay))
                    else:
                        flag = True
                        logger.info("Positioned the element {}[{}].".format(locate, index))
                        return element
            except WebDriverException as e:
                if i == max_times - 1:
                    error = True
                    logger.error(e)
                    raise WebDriverException(e.msg, self.daf.get_screenshot(self.driver))
                if index == None:
                    logger.info(
                        "The elements {} are not successfully positioned and will be retried after hibernation.".format(
                            locate))
                else:
                    logger.info(
                        "The element {}[{}] is not successfully positioned and will be retried after hibernation.".format(
                            locate, index))
            finally:
                if i < max_times - 1 and flag != True:
                    self.sleep(delay)
                elif i == max_times - 1 and error != True:
                    if index == None:
                        logger.error("Failed to position the elements {}!".format(locate))
                        raise WebDriverException("Failed to position the elements {}!".format(locate))
                    else:
                        logger.error("Failed to position the element {}[{}]!".format(locate, index))
                        raise WebDriverException("Failed to position the element {}[{}]!".format(locate, index))

    def wait(self, locate, index=0, max_times=20, delay=0.5, displayed=True):
        """
        等待元素出现
        :param locate: 元素定位
        :param index: 序号，第一个为0，第二个为1，以此类推，默认为0
        :param max_times: 最大循环次数，默认为20次
        :param delay: 延时，默认为0.5秒
        :param displayed: 是否必须等待到元素可见才算找到元素，默认为是
        :return:
        """
        try:
            logger.info("wait ElementOperation displayed")
            self.find_element(locate, index, max_times, delay, displayed=displayed)
            return True
        except WebDriverException as e:
            if 'Failed to position' in e.msg:
                return False
            else:
                raise e
        except Exception as e:
            raise e

    def wait_gone(self, locate, index=0, max_times=20, delay=0.5, displayed=True):
        """
        等待元素消失
        :param locate: 元素定位
        :param max_times: 最大循环次数，默认为20次
        :param index: 序号，第一个为0，第二个为1，以此类推，默认为0
        :param delay: 延时，默认为0.5秒
        :param displayed: 是否必须等待到元素可见才算找到元素，默认为是
        :return:
        """
        for i in range(max_times):
            try:
                self.find_element(locate, index, 1, delay, displayed)
                if i < max_times - 1:
                    self.sleep(delay)
                else:
                    return False
            except WebDriverException as e:
                if 'Failed to position' in e.msg:
                    logger.info("The element {} has been gone.".format(locate))
                    return True
                else:
                    raise e
            except Exception as e:
                raise e

    def exists(self, locate, index=0, max_times=10, delay=0.5, displayed=True):
        """
        检查当前时刻元素是否存在
        :param locate:
        :param index: 序号，第一个为0，第二个为1，以此类推，默认为0
        :param displayed: 是否必须等待到元素可见才算找到元素，默认为是
        :return:
        """
        try:
            self.find_element(locate, index, max_times, delay, displayed=displayed)
            return True
        except:
            return False

    def send_keys(self, locate, text, index=0, max_times=20, delay=0.5, displayed=True):
        """
         输入文本，用于需要定位页面上有多个属性相同的元素中的某一个元素或对应所有元素的情况
        :param locate: 元素定位
        :param text: 需要输入的文本内容
        :param index: 序号，第一个为0，第二个为1，以此类推，默认为0
        :param max_times: 最大循环次数，默认为20次
        :param delay: 延时，默认为0.5秒
        :param displayed: 是否必须等待到元素可见才算找到元素，默认为True
        :return:
        """
        elements = self.find_element(locate, index, max_times, delay, displayed)
        if index != None:
            try:
                elements.clear()
                elements.send_keys(text)
                logger.info("SendKeys  -->  {}[{}] success".format(locate, index))
            except WebDriverException as e:
                logger.error(
                    "SendKeys  -->  {}[{}] failure\nFailed to send_keys to element with {}".format(locate, index, e))
                raise WebDriverException(self.daf.get_screenshot(self.driver))
        else:
            for i, element in enumerate(elements):
                try:
                    element.clear()
                    element.send_keys(text)
                    logger.info("SendKeys  -->  {}[{}] success".format(locate, i))
                except WebDriverException as e:
                    logger.error(
                        "SendKeys  -->  {}[{}] failure\nFailed to send_keys to element with {}".format(locate, i, e))
                    raise WebDriverException(self.daf.get_screenshot(self.driver))

    def clear(self, locate, index=0, max_times=20, delay=0.5, displayed=True):
        """
        清除文本框，用于需要定位页面上有多个属性相同的元素中的某一个元素或对应所有元素的情况
        :param locate: 元素定位
        :param index: 序号，第一个为0，第二个为1，以此类推，默认为0
        :param max_times: 最大循环次数，默认为20次
        :param delay: 延时，默认为0.5秒
        :param displayed: 是否必须等待到元素可见才算找到元素，默认为True
        :return:
        """
        elements = self.find_element(locate, index, max_times, delay, displayed)
        if index != None:
            try:
                elements.clear()
                logger.info("Clear  -->  {}[{}] success".format(locate, index))
            except WebDriverException as e:
                logger.error("Clear  -->  {}[{}] failure\nFailed to clear to element with {}".format(locate, index, e))
                raise WebDriverException(self.daf.get_screenshot(self.driver))
        else:
            for i, element in enumerate(elements):
                try:
                    element.clear()
                    logger.info("Clear  -->  {}[{}] success".format(locate, i))
                except WebDriverException as e:
                    logger.error("Clear  -->  {}[{}] failure\nFailed to clear to element with {}".format(locate, i, e))
                    raise WebDriverException(self.daf.get_screenshot(self.driver))

    def click(self, locate, index=0, max_times=20, delay=0.5, displayed=True):
        """
        点击元素,用于需要定位页面上有多个属性相同的元素中的某一个元素或对应所有元素的情况
        :param locate: 元素定位
        :param index: 序号，第一个为0，第二个为1，以此类推，默认为0
        :param max_times: 最大循环次数，默认为20次
        :param delay: 延时，默认为0.5秒
        :param displayed: 是否必须等待到元素可见才算找到元素，默认为True
        :return:
        """
        elements = self.find_element(locate, index, max_times, delay, displayed)
        if index != None:
            try:
                elements.click()
                logger.info("Click  -->  {}[{}] success".format(locate, index))
            except ElementNotInteractableException:
                self.execute_script("arguments[0].click;", elements)
                logger.info("Click  -->  {}[{}] success".format(locate, index))
            except WebDriverException as e:
                logger.error("Click  -->  {}[{}] failure\nFailed to click the element with {}".format(locate, index, e))
                raise WebDriverException(self.daf.get_screenshot(self.driver))
        else:
            for i, element in enumerate(elements):
                try:
                    element.click()
                    logger.info("Click  -->  {}[{}] success".format(locate, i))
                except WebDriverException as e:
                    logger.error("Click  -->  {}[{}] failure\nFailed to click the element with {}".format(locate, i, e))
                    raise WebDriverException(self.daf.get_screenshot(self.driver))

    def delete(self, locate, index=0, max_times=20, delay=0.5, displayed=True):
        """
        清空test框的数据
        :param locate: 元素定位
        :param index: 序号，第一个为0，第二个为1，以此类推，默认为0
        :param max_times: 最大循环次数，默认为20次
        :param delay: 延时，默认为0.5秒
        :param displayed: 是否必须等待到元素可见才算找到元素，默认为True
        :return:
        """
        elements = self.find_element(locate, index, max_times, delay, displayed)
        if index != None:
            try:
                elements.send_keys(Keys.CONTROL, 'a')
                elements.send_keys(Keys.DELETE)
                logger.info("Delete  -->  {}[{}] success".format(locate, index))
            except ElementNotInteractableException:
                self.execute_script("arguments[0].delete;", elements)
                logger.info("Delete  -->  {}[{}] success".format(locate, index))
            except WebDriverException as e:
                logger.error(
                    "Delete  -->  {}[{}] failure\nFailed to delete the element with {}".format(locate, index, e))
                raise WebDriverException(self.daf.get_screenshot(self.driver))
        else:
            for i, element in enumerate(elements):
                try:
                    elements.send_keys(Keys.CONTROL, 'a')
                    elements.send_keys(Keys.DELETE)
                    logger.info("Delete  -->  {}[{}] success".format(locate, i))
                except WebDriverException as e:
                    logger.error(
                        "Delete  -->  {}[{}] failure\nFailed to delete the element with {}".format(locate, i, e))
                    raise WebDriverException(self.daf.get_screenshot(self.driver))

    def wait_text(self, locate, text, index=0, max_times=20, delay=0.5, displayed=True):
        """
        等待元素的文本内容变成希望出现的文本内容，用于需要定位页面上有多个属性相同的元素中的某一个元素或对应所有元素的情况
        :param locate: 元素定位
        :param text: 希望出现的文本内容，在本方法中该参数可以是字符串或列表，为字符串时表示等待目标元素列表的文本内容等于text，为列表时表示等待目标元素与text的文本内容一一对应且相等
        :param index: 序号，第一个为0，第二个为1，以此类推，默认为None，为默认值时表示等待所有目标元素的文本内容变成希望出现的文本内容
        :param max_times: 最大循环次数，默认为20次
        :param delay: 延时，默认为0.5秒
        :param displayed: 是否必须等待到元素可见才算找到元素，默认为True
        :return:
        """
        for i in range(max_times):
            num = 0
            if index != None:
                elements_text = self.find_element(locate, index, max_times, delay, displayed).text
            else:
                elements_text = [element.text for element in
                                 self.find_element(locate, index, max_times, delay, displayed)]
            logger.info(
                'The text of the target element is "{}",the actual text is "{}"...\nStart matching>>>>>>'.format(text,
                                                                                                                 elements_text))
            if type(text) == list:
                if type(elements_text) == list and len(text) != len(elements_text):
                    logger.error(
                        "The length of the entered text list({}) is inconsistent with the actual list({}).".format(
                            len(text), len(elements_text)))
                    raise Exception(
                        "The length of the entered text list({}) is inconsistent with the actual list({}).".format(
                            len(text), len(elements_text)))
                elif type(elements_text) == str and len(text) != 1:
                    logger.error(
                        "The length of the entered text list({}) is inconsistent with the actual string(1).".format(
                            len(text)))
                    raise Exception(
                        "The length of the entered text list({}) is inconsistent with the actual string(1).".format(
                            len(text)))
                if type(elements_text) == list:
                    for j, element_text in enumerate(elements_text):
                        if element_text == text[j]:
                            num += 1
                        elif element_text != text[j] and i < max_times - 1:
                            self.sleep(delay)
                            break
                        else:
                            logger.error('Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
                            raise WebDriverException(
                                'Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
                    if num == len(elements_text):
                        logger.info('Matching success！')
                        break
                elif type(elements_text) == str:
                    if elements_text == text[0]:
                        logger.info('Matching success！')
                        break
                    elif i < max_times - 1:
                        self.sleep(delay)
                    else:
                        logger.error('Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
                        raise WebDriverException(
                            'Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
            elif type(text) == str:
                if type(elements_text) == list:
                    for j, element_text in enumerate(elements_text):
                        if element_text == text:
                            num += 1
                        elif element_text != text and i < max_times - 1:
                            self.sleep(delay)
                            break
                        else:
                            logger.error('Matching Failed!\nTarget : {} \nActual : {}'.format(text, element_text))
                            raise WebDriverException(
                                'Matching Failed!\nTarget : {} \nActual : {}'.format(text, element_text))
                    if num == len(elements_text):
                        logger.info('Matching success！')
                        break
                elif type(elements_text) == str:
                    if elements_text == text:
                        logger.info('Matching success！')
                        break
                    elif i < max_times - 1:
                        self.sleep(delay)
                    else:
                        logger.error('Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
                        raise WebDriverException(
                            'Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
            else:
                logger.warn(
                    'Entered the wrong value of text, please check the value of it !\ntext type:{}\ntext value:{}'.format(
                        type(text), text))
                raise Exception(
                    'Entered the wrong value of text, please check the value of it !\ntext type:{}\ntext value:{}'.format(
                        type(text), text))

    def wait_text_gone(self, locate, text, index=0, max_times=20, delay=0.5, displayed=True):
        """
        等待元素的文本内容变更
        :param locate: 元素定位
        :param text: 希望消失的文本内容，在本方法中该参数可以是字符串或列表，为字符串时表示等待目标元素的文本内容不包含text，为列表时表示等待目标元素与text的文本内容一一对应且不相等
        :param index: 序号，第一个为0，第二个为1，以此类推，默认为None，为默认值时表示等待所有目标元素的文本内容变更
        :param max_times: 最大循环次数，默认为20次
        :param delay: 延时，默认为0.5秒
        :param displayed: 是否必须等待到元素可见才算找到元素，默认为True
        :return:
        """
        for i in range(max_times):
            num = 0
            try:
                if index != None:
                    elements_text = self.find_element(locate, index, max_times, delay, displayed).text
                else:
                    elements_text = [element.text for element in
                                     self.find_element(locate, index, max_times, delay, displayed)]
            except WebDriverException as e:
                if i < max_times - 1:
                    continue
                else:
                    raise e
            logger.info(
                'The text of the target element is "{}",the actual text is "{}"...\nStart matching>>>>>>'.format(text,
                                                                                                                 elements_text))
            if type(text) == list:
                if type(elements_text) == list and len(text) != len(elements_text):
                    logger.info('Matching success！')
                    break
                if type(elements_text) == str and len(text) != 1:
                    logger.error(
                        "The length of the entered text list({}) is inconsistent with the actual string(1).".format(
                            len(text)))
                    raise Exception(
                        "The length of the entered text list({}) is inconsistent with the actual string(1).".format(
                            len(text)))
                if type(elements_text) == list:
                    for j, element_text in enumerate(elements_text):
                        if element_text != text[j]:
                            num += 1
                        elif element_text == text[j] and i < max_times - 1:
                            self.sleep(delay)
                            break
                        else:
                            logger.error('Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
                            raise WebDriverException(
                                'Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
                    if num == len(elements_text):
                        logger.info('Matching success！')
                        break
                elif type(elements_text) == str:
                    if elements_text != text[0]:
                        logger.info('Matching success！')
                        break
                    elif i < max_times - 1:
                        self.sleep(delay)
                    else:
                        logger.error('Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
                        raise WebDriverException(
                            'Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
            elif type(text) == str:
                if type(elements_text) == list:
                    for j, element_text in enumerate(elements_text):
                        if element_text != text:
                            num += 1
                        elif element_text == text and i < max_times - 1:
                            self.sleep(delay)
                            break
                        else:
                            logger.error('Matching Failed!\nTarget : {} \nActual : {}'.format(text, element_text))
                            raise WebDriverException(
                                'Matching Failed!\nTarget : {} \nActual : {}'.format(text, element_text))
                    if num == len(elements_text):
                        logger.info('Matching success！')
                        break
                elif type(elements_text) == str:
                    if elements_text != text:
                        logger.info('Matching success！')
                        break
                    elif i < max_times - 1:
                        self.sleep(delay)
                    else:
                        logger.error('Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
                        raise WebDriverException(
                            'Matching Failed!\nTarget : {} \nActual : {}'.format(text, elements_text))
            else:
                logger.warn(
                    'Entered the wrong value of text, please check the value of it !\ntext type:{}\ntext value:{}'.format(
                        type(text), text))
                raise Exception(
                    'Entered the wrong value of text, please check the value of it !\ntext type:{}\ntext value:{}'.format(
                        type(text), text))

# if __name__ == '__main__':
#     if 1 and None or 1 and None:
#         print(1)
