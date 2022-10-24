import datetime


class RangeDate:
    def __init__(self):
        pass

    def get_date_iter(self, start_date, end_date):
        """
        获取指定时间段内的日期
        :param self: 起始时间 --> str YYYYmmdd
        :param end_date: 结束时间 --> str YYYYmmdd
        :return: iter
        """
        dt = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        list_date = []
        date = dt.strftime("%Y-%m-%d")
        list_date.append(date)
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        while dt < end_date:
            dt = dt + datetime.timedelta(days=1)
            date = dt.strftime("%Y-%m-%d")
            list_date.append(date)
        return list_date