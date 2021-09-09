import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

from run_eval import run_generate

st.write('# GupShup')
st.write('## Summarizing Open-Domain Code-Switched Conversations')
task_type= st.sidebar.selectbox(
    'Task type',["English to English","English to Hindi"]
)
model_name= st.sidebar.selectbox(
    'Model',["Pegasus","mBart"]
)

src_form = st.sidebar.form(key='src_form')
src_ip=src_form.text_input(label='Please enter path to conversastion/source file')
tar_ip=src_form.text_input(label='Please enter path to summary/target file. [optional]')
src_submit_button = src_form.form_submit_button(label='Submit')
st.sidebar.markdown("<h1 style='text-align: center;'>OR</h1>", unsafe_allow_html=True)
# st.sidebar.write("### Or")
# tar_form = st.sidebar.form(key='tar_form')
# tar_ip=tar_form.text_input(label='Please enter path to the summary file')
# tar_submit_button = tar_form.form_submit_button(label='Submit')

conv_form = st.sidebar.form(key='conv_form')
conv_ip=conv_form.text_input(label='Please enter the conversastion')
conv_submit_button = conv_form.form_submit_button(label='Submit')
st.write('### Task Type:', task_type)
st.write('### Model:', model_name)
x= "fg"

src_file= None
tar_file= None
gen_file= None
score_file= None



if conv_submit_button:
    if conv_ip=="":
        st.write("Pls enter non empty conversastion")
        
    else:
        st.write( "### Summarizing below Conversastion")
        st.write(conv_ip)
        src_file= 'conversastion.txt'
        src_fp= open(src_file,'w')
        src_fp.write(conv_ip)
        src_fp.close()
        st.write( "### Summary")
        x= "conv"


if src_submit_button:
    st.write(" src and tar")
    st.write(src_ip)
    st.write(tar_ip, type(tar_ip))
    if tar_ip!="":
        gen_file= "generated_summary.txt"
        score_file= "scores.txt"
        # st.write("tar is empty")
    x= "files"


run_generate(
    verbose=True,
    model_name_path= model_name,
    src_txt= src_file,
    tar_txt= tar_file,
    gen_path=gen_file,
    scor_path=score_file,
    batch_size= None
)

st.write(x)
