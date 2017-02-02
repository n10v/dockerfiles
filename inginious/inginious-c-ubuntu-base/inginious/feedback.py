# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

import json
import os
import sys

def load_feedback():
    """ Open existing feedback file """
    result = {}
    if os.path.exists('/.__output/__feedback.json'):
        f = open('/.__output/__feedback.json', 'r')
        cont = f.read()
        f.close()
    else:
        cont = '{}'
    try:
        result = json.loads(cont) if cont else {}
    except ValueError as e:
        result = {"result":"crash", "text":"Feedback file has been modified by user !"}
    return result

def save_feedback(rdict):
    """ Save feedback file """
    # Check for output folder
    if not os.path.exists('/.__output'):
        os.makedirs('/.__output/')
    
    jcont = json.dumps(rdict)
    f = open('/.__output/__feedback.json', 'w')
    f.write(jcont)
    f.close()

# Doing the real stuff
def set_global_result(result):
    """ Set global result value """
    rdict = load_feedback()
    rdict['result'] = result
    save_feedback(rdict)

def set_problem_result(result, problem_id):
    """ Set problem specific result value """
    rdict = load_feedback()
    if not 'problems' in rdict:
        rdict['problems'] = {}
    cur_val = rdict['problems'].get(problem_id, '')
    rdict['problems'][problem_id] = [result, cur_val] if type(cur_val) == str else [result, cur_val[1]]
    save_feedback(rdict)

def set_grade(grade):
    """ Set global grade of this job """
    rdict = load_feedback()
    rdict['grade'] = float(grade)
    save_feedback(rdict)

def set_global_feedback(feedback, append=False):
    """ Set global feedback in case of error """
    rdict = load_feedback()
    rdict['text'] = rdict.get('text', '') + feedback if append else feedback
    save_feedback(rdict)

def set_problem_feedback(feedback, problem_id, append=False):
    """ Set problem specific feedback """
    rdict = load_feedback()
    if not 'problems' in rdict:
        rdict['problems'] = {}
    cur_val = rdict['problems'].get(problem_id, '')
    rdict['problems'][problem_id] = (cur_val + feedback if append else feedback) if type(cur_val) == str else [cur_val[0], (cur_val[1] + feedback if append else feedback)]
    save_feedback(rdict)

def set_custom_value(custom_name, custom_val):
    """
    Set a custom value to be given back in the feedback
    :param custom_name: name/key of the entry to be placed in the custom dict
    :param custom_val: content of the entry to be placed in the custom dict
    """
    rdict = load_feedback()
    if not "custom" in rdict:
        rdict["custom"] = {}
    rdict["custom"][custom_name] = custom_val
    save_feedback(rdict)

def get_feedback():
    """ Returns the dictionary containing the feedback """
    rdict = load_feedback()
    return rdict
