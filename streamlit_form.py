# from ctypes.wintypes import SIZE
from logging import PlaceHolder
import streamlit as st
import json

st.sidebar.write(
    f"Please fill the given form."
)

st.title("SOP Generator Application", anchor=None)
form = st.form(key="annotation")

with form:
    #Personal details
    # st.subheader("Personal details: ")
    s_first_name = st.text_input("First name:")
    s_last_name = st.text_input("Last name:")
    s_email = st.text_input("Email:")
    
    l_codes = json.load(open('country_codes.json'))
    l_country_codes = [d['dial_code'] for d in l_codes]
    
    cols = st.columns((0.5, 1.5))
    country_code = cols[0].selectbox(
        "Country-code:", l_country_codes, index=29
    )
    phone_number = cols[1].text_input("Phone number:") 
    
    countries = json.load(open('country_list.json'))
    l_countries = [d['name'] for d in countries]
    s_dest_market = st.selectbox(
       "Destination market: ", l_countries, index=13
    )
    s_birth_date = st.date_input(
       "Date of birth: "
    )
    s_motivator = st.selectbox(
       "Person motivator for study: ", ["Mother","Father","Grandparents","Brother","Sister","Uncle","Aunt","Others"], index=1
    )
    st.text_input("Others, Please type:")
    
    s_acad_level = st.selectbox(
       "Your academic level: ", ["Undergraduate", "Post-Graduate", "PHD"], index=1
    )
    # Experiance details
    # st.subheader("Experiance details: ")
    
    #Interships
    st.caption("Internship experiance")
    cols = st.columns((1, 0.5,0.5))
    s_internship_company_1 = cols[0].text_input("Internship 1",placeholder="Company name")
    s_internship_company_1_from =  cols[1].date_input("Internship 1 From")
    s_internship_company_1_to =  cols[2].date_input("Internship 1 To")
    s_internship_company_1_desc =  st.text_area("Internship 1 description",placeholder="Write your internship work in short")
    cols = st.columns((1, 0.5,0.5))
    s_internship_company_2 = cols[0].text_input("Internship 2",placeholder="Company name")
    s_internship_company_2_from =  cols[1].date_input("Internship 2 From")
    s_internship_company_2_to =  cols[2].date_input("Internship 2 To")
    s_internship_company_2_desc =  st.text_area("Internship 2 description",placeholder="Write your internship work in short")
    cols = st.columns((1, 0.5,0.5))
    s_internship_company_3 = cols[0].text_input("Internship 3",placeholder="Company name")
    s_internship_company_3_from =  cols[1].date_input("Internship 3 From")
    s_internship_company_3_to =  cols[2].date_input("Internship 3 To")
    s_internship_company_3_desc =  st.text_area("Internship 3 description",placeholder="Write your internship work in short")
    
    #Job
    st.caption("Job experiance")
    cols = st.columns((1, 0.5,0.5))
    s_job_company_1 = cols[0].text_input("Job 1",placeholder="Company name")
    s_job_company_1_from =  cols[1].date_input("Job 1 From")
    s_job_company_1_to =  cols[2].date_input("Job 1 To")
    s_job_company_1_desc =  st.text_area("Job 1 description",placeholder="Write your Job work in short")
    cols = st.columns((1, 0.5,0.5))
    s_job_company_2 = cols[0].text_input("Job 2",placeholder="Company name")
    s_job_company_2_from =  cols[1].date_input("Job 2 From")
    s_job_company_2_to =  cols[2].date_input("Job 2 To")
    s_job_company_2_desc =  st.text_area("Job 2 description",placeholder="Write your Job work in short")
    cols = st.columns((1, 0.5,0.5))
    s_job_company_3 = cols[0].text_input("Job 3",placeholder="Company name")
    s_job_company_3_from =  cols[1].date_input("Job 3 From")
    s_job_company_3_to =  cols[2].date_input("Job 3 To")
    s_job_company_3_desc =  st.text_area("Job 3 description",placeholder="Write your Job work in short")
    
    #Research
    st.caption("Research experiance")
    cols = st.columns((1, 0.5,0.5))
    s_research_company_1 = cols[0].text_input("Research 1",placeholder="Research 1 title")
    s_research_company_1_from =  cols[1].date_input("Research 1 From")
    s_research_company_1_to =  cols[2].date_input("Research 1 To")
    s_research_company_1_desc =  st.text_area("Research 1 description",placeholder="Write your research work in short")
    cols = st.columns((1, 0.5,0.5))
    s_research_company_2 = cols[0].text_input("Research 2",placeholder="Research 2 title")
    s_research_company_2_from =  cols[1].date_input("Research 2 From")
    s_research_company_2_to =  cols[2].date_input("Research 2 To")
    s_research_company_2_desc =  st.text_area("Research 2 description",placeholder="Write your research work in short")
    cols = st.columns((1, 0.5,0.5))
    s_research_company_3 = cols[0].text_input("Research 3",placeholder="Research 3 title")
    s_research_company_3_from =  cols[1].date_input("Research 3 From")
    s_research_company_3_to =  cols[2].date_input("Research 3 To")
    s_research_company_3_desc =  st.text_area("Research 3 description",placeholder="Write your research work in short")
    
    
    #Personal projects
    st.caption("Personal projects")
    cols = st.columns((0.5, 1.5))
    s_research_company_1 = cols[0].text_input("Personal project 1",placeholder="title")
    s_research_company_1_desc = cols[1].text_area("Personal project 1 description",placeholder="Write your Personal project work in short")
    cols = st.columns((0.5, 1.5))
    s_research_company_2 = cols[0].text_input("Personal project 2",placeholder="title")
    s_research_company_2_desc =  cols[1].text_area("Personal project 2 description",placeholder="Write your Personal project work in short")
    cols = st.columns((0.5, 1.5))
    s_research_company_3 = cols[0].text_input("Personal project 3",placeholder="title")
    s_research_company_3_desc =  cols[1].text_area("Personal project 3 description",placeholder="Write your Personal project work in short")
    
    s_interest = st.text_area("Interst",placeholder="Write your interest")
    s_motivation = st.text_area("Motivation",placeholder="Write your motivation")
    
    s_license_1 = st.text_input("Licence/certification 1")
    s_license_2 = st.text_input("Licence/certification 2")
    s_license_3 = st.text_input("Licence/certification 3")
    
    st.caption("Publications")
    cols = st.columns((0.5, 0.5 ,1))
    s_publication_1 = cols[0].text_input("Publication 1",placeholder="Publication title")
    s_publication_1_date = cols[1].date_input("Publication 1 date")
    s_publication_1_desc = cols[2].text_area("Publication 1 description",placeholder="Write your publication work")
    cols = st.columns((0.5, 0.5 ,1))
    s_publication_2 = cols[0].text_input("Publication 2",placeholder="Publication title")
    s_publication_2_date = cols[1].date_input("Publication 2 date")
    s_publication_2_desc = cols[2].text_area("Publication 2 description",placeholder="Write your publication work")
    cols = st.columns((0.5, 0.5 ,1))
    s_publication_3 = cols[0].text_input("Publication 3",placeholder="Publication title")
    s_publication_3_date = cols[1].date_input("Publication 3 date")
    s_publication_3_desc = cols[2].text_area("Publication 3 description",placeholder="Write your publication work")
    
    s_achievement_1 = st.text_input("Achievement 1")
    s_achievement_2 = st.text_input("Achievement 2")
    s_achievement_3 = st.text_input("Achievement 3")
    
    s_highlight = st.text_area("Highlights: ",placeholder="Write your key highlight points")
    
    s_target_acad_level = st.selectbox(
       "Target academic level: ", ["PG","PHD","MBA","Internship"], index=1
    )
    s_target_university = st.selectbox(
       "Target academic level: ", ["Univ 1","Univ 2","Univ 3","Univ 4"], index=1
    )
    s_target_department = st.selectbox(
       "Target academic level: ", ["dep 1","dep 2","dep 3","dep 4"], index=1
    )
    
    s_target_research = st.text_input("Target Research")
    s_target_professor = st.text_input("Target Professor")
    bool_funding = st.checkbox("You need funding?")
    
    s_target_scholarship = st.text_input("Target scholarship: ")
    
    st.caption("Exam scores")
    cols = st.columns((0.5, 0.5))
    s_exam_1 = cols[0].selectbox(
       "Exam 1: ",["TOEFL", "GRE", "GMAT", "ELTS", "SAT"], index=1,
    )
    i_score_exam_1 = cols[1].number_input(
       "Exam 1 score: ", step=1
    )
    s_exam_2 = cols[0].selectbox(
       "Exam 2: ", ["TOEFL", "GRE", "GMAT", "ELTS", "SAT"], index=0
    )
    i_score_exam_2 = cols[1].number_input(
       "Exam 2 score: ",step=1
    )
    submitted = st.form_submit_button(label="Submit")


if submitted:
    st.success("Thanks! Your bug was recorded.")
    st.balloons()

expander = st.expander("See all records")
