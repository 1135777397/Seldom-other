# COMMON_FUNCTION(公共方法)
## logger.py
> 封装日志打印
### 日志文件存储路径
**__init__**:指定保存日志的文件路径，日志级别，以及调用文件将日志存入到指定的文件中
  
- self.path:  路径为当前文件上一级再上一级/logs
- time_with_Y_m_d: 时间格式2022-03-02
- time_with_Y_m_d_H: 时间格式2022-03-02_15
- dir_path: self.path+时间命名文件夹
- 判断文件夹是否存在，不存在则创建

**日志文件名**

每相差两小时新建一个日志文件，如果没有文件，那就创建一个文件

设置的日志处理器级别都为INFO,日志器为debug


## dateTimeTool.py
>日期时间工具方法

DateTimeTool
- getNowTime 
  - 获取当前时间，按照xxxx-xx-xx xx:xx:xx格式
- getNowDate 
  - 获取当前日期，按照xxxx-xx-xx格式 
- getNowTimeStampWithSecond 
  - 返回带秒的时间戳 
- getNowTimeStampWithMillisecond 
  - 返回带毫秒的时间戳 
- timeStampToDateTime 
  - 返回当前时间 
- getWeekDay 
  - 获得今天星期几，从1开始 
- getHowDaysAgo 
  - 显示几天前日期 
- dateTimeToStr 
  - 将时间转成str模式，格式化日期 
- strToDateTime 
  - 解析日期 
- getHowYearsAgo 
  - 显示几年前日期 
- getCurrentMonthFirstDayOrLastDay 
  - 获取当前月第一天或者最后一天日期
