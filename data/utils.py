import ast

def generate_url(path: list, params: dict = None):
    url = '/'.join(list(filter(None, path)))
    if params:
        param = str()
        for key, value in params.items():
            param += '='.join([key, str(value)]) + '&'
        return '?'.join([url, param])[0:-1]
    return url


def str_to_dict(data):
    return ast.literal_eval(
        data
        .replace('null', "'null'")
        .replace('false', "'false'")
        .replace('true', "'true'")
        .replace('\/', "/")
        .replace('<br />', '')
    )


def str2bool(text:str):
    return text.lower() in ("yes", "true", "t", "1")


def merge_lang(en:list, ru:list, field:str):
    key_idx = [
        i for i, s in enumerate([x.lower() for x in list(en[0].keys())]) if field in s
    ][0]
    for idx, item in enumerate(en):
        en[idx][f'ru_{field}'] = ru[idx][list(ru[idx].keys())[key_idx]]
    return en
