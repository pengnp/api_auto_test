from functools import wraps
import logging


def request_check(func):
    @wraps(func)
    def check(*args, **kwargs):
        if args[2] not in ['get', 'post', 'put', 'delete', 'patch']:
            raise ValueError(f'不存在该请求方式: {args[2]}')
        rep = func(*args, **kwargs)
        if rep.status_code != 200:
            raise ValueError(f'接口请求异常, 当前状态码为: {rep.status_code}')
        logging.info(f'接口 {args[1]} 请求成功, 返回值为: {rep.text}')
        return rep
    return check

