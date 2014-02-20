# -*- coding: utf-8 -*-


from flask import flash, jsonify, json

class DaixieError(Exception):
    pass

def get_msg(msg):
    if isinstance(msg, (str, unicode)):
        return msg
    elif isinstance(msg, Exception):
        return msg.message

def success(msg):
    flash(get_msg(msg), 'success')

def fail(e):
    flash(get_msg(e), 'danger')

def j_response(status, msg, raw=False, **kwargs):
    kwargs['status'] = status
    kwargs['msg'] = get_msg(msg)
    return json.dumps(kwargs) if raw else jsonify(**kwargs)

def j_ok(msg, raw=False, **kwargs):
    return j_response('ok', msg, raw, **kwargs)

def j_err(e, raw=False, **kwargs):
    return j_response('error', e, raw, **kwargs)

def j_redirect(msg, raw=False, **kwargs):
    return j_response('redirect', msg, raw, **kwargs)