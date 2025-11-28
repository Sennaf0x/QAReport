import streamlit as st
from datetime import datetime
import pandas as pd


markdown_report = ""

# Função que gera markdown detalhado do dataframe Excel/CSV
def gerar_markdown_relatorio_excel(df):
    colunas_esperadas = ["User Story", "Executed", "Pass", "Fail", "Not Run", "Build", "Result", "Tester", "Comments"]
    if not all(col in df.columns for col in colunas_esperadas):
        st.error(f"O arquivo deve conter as colunas: {colunas_esperadas}")
        return None

    markdown = (
        "| **User Story** | Executed | Pass | Fail | Not Run | Build | Result | Tester | Comments |\n"
        "|----------------|:----:|:----:|:----:|:--:|:-----:|:-------:|---------|----------|\n"
    )
    for _, row in df.iterrows():
        user_story = str(row["User Story"]).replace("|", r"\|")
        executed = int(row["Executed"])
        passed = int(row["Pass"])
        failed = int(row["Fail"])
        not_run = int(row["Not Run"])
        build = row["Build"]
        result = row["Result"]
        tester = row["Tester"]
        comments = row["Comments"] if pd.notna(row["Comments"]) else "-"

        markdown += f"| {user_story} | {executed} | {passed} | {failed} | {not_run} | {build} | {result} | {tester} | {comments} |\n"
    return markdown

def gerar_sumario_execucao(df):
    """
    A partir de um dataframe no formato esperado, calcula o sumário de execução
    dos testes e retorna uma string em markdown com a tabela de resumo.
    """
    colunas_esperadas = ["Executed", "Pass", "Fail", "Not Run"]
    if not all(col in df.columns for col in colunas_esperadas):
        raise ValueError(f"O DataFrame deve conter as colunas: {colunas_esperadas}")

    total_passed = df["Pass"].sum()
    total_failed = df["Fail"].sum()
    total_not_run = df["Not Run"].sum()
    total_executed = total_passed + total_failed - total_not_run
    total_test_cases = total_passed + total_failed + total_not_run

    markdown_summary = "### 2.2 Execution Summary\n"
    markdown_summary += "| **Metric**         | **Value** |\n"
    markdown_summary += "|--------------------|-----------|\n"
    markdown_summary += f"| Total Test Cases   | **{total_test_cases}** |\n"
    markdown_summary += f"| Executed           | **{total_executed}** |\n"
    markdown_summary += f"| Passed             | **{total_passed}** |\n"
    markdown_summary += f"| Failed             | **{total_failed}** |\n"
    markdown_summary += f"| Not Run            | **{total_not_run}** |\n"

    return markdown_summary

# Configurar a página para usar layout widescreen
st.set_page_config(layout="wide")

st.title("Sprint Tests Report")

col1, col2, col3 = st.columns(3)

test_types = [
    "Business rule",
    "Layout / UI",
    "Verification",
    "Exploratory",
    "Regression",
    "Automated",
    "Performance",
]

with st.form("report_form"):
        with col1:
            version = st.text_input("Version", "3.1")
            sprint = st.text_input("Sprint", "Sprint 36")
            report_date = st.date_input("Report Date", datetime.strptime("11/04/2025", "%m/%d/%Y"))
            environment = st.selectbox("Environment", ["QA", "Production", "Staging"], index=0)
            sprint_window = st.text_input("Sprint Window", "10/29/25 → 11/04/25")

        with col2:
            status = st.selectbox(
                "Status",
                options=["Success", "Fail", "Not Run"],
                format_func=lambda x: {
                    "Success": "🟢 Success",
                    "Fail": "🔴 Fail",
                    "Not Run": "⚪ Not Run",
                }[x],
                index=0,
            )
            project = st.text_input("Project", "Tester Performance")
            analyst = st.text_input("Analyst", "Paulo Senna Taylor Bittencourt")
            release_notes = st.text_input(
                "Release Notes",
                "https://dev.azure.com/VNT-MAO-Jabil/Tester%20Performance/_wiki/wikis/Tester-Performance.wiki/1282/Version-3.16",
            )
            acceptance_criteria = st.text_input(
                "Acceptance Criteria",
                "https://dev.azure.com/VNT-MAO-Jabil/Tester%20Performance/_wiki/wikis/Tester-Performance.wiki/1107/Version-2.9.0",
            )
        with col3:    
            selected_tests = st.multiselect(
                "Select test types executed (checked = True)",
                options=test_types,
                default=[
                    "Business rule",
                    "Layout / UI",
                    "Verification",
                    "Exploratory",
                    "Regression",
                ],
            )

            text_summary = st.text_area("Summary","All tests executed **with success**, except the story *1292881 — GR&R | Label Update for Missing Requirements Button*, which was moved to the next sprint.")

            uploaded_file = st.file_uploader(
                "Upload Excel ou CSV dos casos de teste",
                type=['xlsx', 'xls', 'csv']
            )

            df_uploaded = None
            if uploaded_file is not None:
                try:
                    if uploaded_file.name.endswith(('xls', 'xlsx')):
                        df_uploaded = pd.read_excel(uploaded_file)
                    else:
                        df_uploaded = pd.read_csv(uploaded_file)

                    st.write("Preview of uploaded file:")
                    st.dataframe(df_uploaded)
                except Exception as e:
                    st.error(f"Erro ao ler o arquivo: {e}")

        submitted = st.form_submit_button("Submit")

if submitted:
    tests = {test: (test in selected_tests) for test in test_types}
    status_emoji = {"Success": "🟢", "Fail": "🔴", "Not Run": "⚪"}[status]

    markdown_report = f"""# Sprint Tests Report — Version {version} ({sprint})

**Report Date:** {report_date.strftime('%m/%d/%Y')}  
**Environment:** {environment}  
**Sprint Window:** {sprint_window}  
**Status:** {status_emoji} {status}

---

## 1. Overview

| **Project**   | {project}                                   |
|--------------|---------------------------------------------|
| **Analyst**   | {analyst}                                   |
| **Release Notes**       | [{sprint}]({release_notes})                   |
| **Acceptance Criteria** | [Test Plan Report]({acceptance_criteria})    |

### 1.1. 🔎 Summary Result

{text_summary}

---

## 2. Test Coverage

### 2.1 Types of Tests Executed
"""

    for test_name, executed in tests.items():
        checkbox = "☑️" if executed else "⬜"
        markdown_report += f"- {checkbox} {test_name}\n"


# ... aqui pode adicionar o markdown detalhado como já faz no seu código ...
if df_uploaded is not None:
    markdown_sumario = gerar_sumario_execucao(df_uploaded)
    markdown_report += markdown_sumario
    
    markdown_detalhado = gerar_markdown_relatorio_excel(df_uploaded)
    markdown_report += "\n---\n\n### 2.3 Detailed Test Cases\n\n"
    markdown_report += markdown_detalhado


markdown_report += """
🟢 **Pass** — Test case executed and passed  
🔴 **Fail** — Test case executed and failed  
⚪ **Not Run** — Test case not executed during this sprint
"""

st.markdown(markdown_report)