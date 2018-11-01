# coding=utf-8
# 爬虫框架/core/pipeline.py
"""管道组件封装"""


class Pipeline:
    """负责处理数据对象"""
    def process_item(self, item):
        print("item:", item)
