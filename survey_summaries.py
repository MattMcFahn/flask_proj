# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:39:13 2020

@author: mattm
"""

import psycopg2
import matplotlib.pyplot as plt
import math

submission_categories = ['Python (of course)', 'Ruby','Java','C','Javascript']

def __set_natural_y_range__(observed_range):
    """
    sends dict vals to a pairing 
    """
    max_y = max(observed_range)
    y_axis_lim = int(math.ceil(max_y / 10.0)) * 10
    step_size = int(y_axis_lim / 10)
    y_axis_ticks = [x for x in range(0,y_axis_lim + step_size, step_size)]
    return(y_axis_ticks)

def retrieve_survey_data():
    sql_uri = r'postgres://ojsogizyxpmsht:2b62fd599fbac77125c5991edccf4d10f811fce0e72f9765597bfb8fac10d5df@ec2-174-129-255-15.compute-1.amazonaws.com:5432/d4ou5ir17dk44p?sslmode=require'
    conn = psycopg2.connect(sql_uri, sslmode='require')
    # Retrieve the cursor
    cur = conn.cursor()
    
    GROUBY_QUERY = '''SELECT submission_, COUNT(*) FROM survey_data GROUP BY (submission_);'''
    cur.execute(GROUBY_QUERY)
    list_records = cur.fetchall()
    
    survey_data = {}
    for submission_category_id in range(0, len(list_records)):
        submission_category = list_records[submission_category_id][0]
        number_submissions = list_records[submission_category_id][1]
        survey_data[submission_category] = number_submissions
        
    
    for submission_category in submission_categories:
        if submission_category not in survey_data:
            survey_data[submission_category] = 0
    return survey_data

def survey_summary_barchart():
    survey_data = retrieve_survey_data()
    x_labels = [ x for x in survey_data.keys()]
    x_labels[0] = 'Python \n (of course)'
    y_range = __set_natural_y_range__(survey_data.values())
    fig = plt.figure(figsize=(5,3.2),dpi=300)
    plt.bar(x = range(0,len(x_labels)),height = survey_data.values())
    plt.title('Summary of survey responses')
    plt.xlabel('Response submission')
    plt.ylabel('Number of responses')
    y_pos = [0,1,2,3,4]
    plt.xticks(y_pos, x_labels, fontsize=9)
    plt.yticks(y_range) #None needs a tuple (,)
    return fig

