import streamlit as st
import numpy as np
import pandas as pd
import os
from run_eval import run_generate

st.write('# GupShup')
st.write('## Summarizing Open-Domain Code-Switched Conversations')
task_type= st.sidebar.selectbox(
    'Task type',["Hindi to English","English to English"]
)
model_name= st.sidebar.selectbox(
    'Model',["Pegasus","mBart","Bart","GPT", "T5", "T5_MTL"]
)

src_form = st.sidebar.form(key='src_form')
src_ip=src_form.text_input(label='Please enter path to conversastion/source file')
tar_ip=src_form.text_input(label='Please enter path to summary/target file. [optional]')
src_submit_button = src_form.form_submit_button(label='Submit')
st.sidebar.markdown("<h1 style='text-align: center;'>OR</h1>", unsafe_allow_html=True)


conv_form = st.sidebar.form(key='conv_form')
conv_ip=conv_form.text_input(label='Please enter the conversastion')
conv_submit_button = conv_form.form_submit_button(label='Submit')
st.write('### Task Type:', task_type)
st.write('### Model:', model_name)
x= "fg"

src_file= None
tar_file= None
gen_file= "generated_summary.txt"
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
        # st.write( "### Summary")
        



if src_submit_button:
    if src_ip=="":
        st.write("### Please enter path to conversastion file")
    elif os.path.isfile(src_ip)==False:
        st.write("### Path to conversastion file is invalid")

    else:
        src_file= src_ip
        st.write("summarizing conversastion stored in ",src_file)
        if tar_ip!="" and os.path.isfile(tar_ip):
            tar_file= tar_ip

            score_file= "scores.txt"
        else:
            st.wrie("Target file is not provided or invalid, score will not be calculated")

    # src and tar file chaeck
    st.write(" src and tar")
    st.write(src_ip)
    st.write(tar_ip)

tt="h2e"
if task_type=="English to English":
    tt="e2e"
elif task_type=="Hindi to English":
    tt="h2e"
model_name_path="midas/gupshup_"+str(tt)+"_"+str(model_name).lower()

if src_file== None or os.path.isfile(src_file)==False:
    st.write("### source file is empty or invalid")
else:

    result= run_generate(
        verbose=True,
        model_name_path= model_name_path,
        src_txt= src_file,
        tar_txt= tar_file,
        gen_path=gen_file,
        scor_path=score_file,
        batch_size= 8
    )

    

    if conv_submit_button:
        st.write("summary:")
        fp= open(gen_file,'r')
        summary= fp.readlines()
        fp.close()
        st.write(summary)

    if src_submit_button:
        if tar_file!=None:
            st.write("scores: ", result)
        
        st.write("summary is stored in ", gen_file)




# st.write(x)
