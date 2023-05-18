<!-- PROJECT NAME -->

<br />
<div align="center">
  <h3 align="center">Model Comparison Workflow on Issue Pull: Weights & Biases</h3>
</div>


<!-- ABOUT PROJECT -->
## What Is It?

This repository contains a Continuous Integration/Continuous Deployment (CI/CD) workflow implemented using GitHub Actions and the Weights and Biases (wandb) platform. The purpose of this workflow is to automatically generate a model comparison report whenever a user creates an issue on GitHub with a specific command in the body. The workflow utilizes the wandb API and reports functionality to compare the performance of a user-specified model run with a predefined baseline run.

By leveraging the wandb platform and GitHub Actions, the workflow offers several benefits:
*  Collaboration and Communication: The workflow is integrated with GitHub Issues, allowing users to easily initiate model comparisons and facilitating collaboration and discussion around the results through issue comments.
*  Efficiency and Automation: With this workflow, users no longer need to manually compare their model runs to a baseline. The comparison is automated, saving time and effort.
*  Standardized Comparison: The workflow ensures a consistent and standardized approach to comparing models by utilizing the same baseline (or any other run as desired) run and report format for all comparisons.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Workflow Overview -->
## Workflow Overview

The CI/CD workflow consists of the following main components:
*   GitHub Issues: Users create issues (type of issues could be passed incase one desires action at certain times) on the GitHub repository, providing details about their model runs and specifying the command for generating the comparison report.
*   GitHub Actions: When a new issue is created (or reopened, or edited), the workflow is triggered and executed on the GitHub Actions platform. The workflow consists of a series of steps defined in a YAML file (named as, <a href='.github/workflows/comparison_workflow.yml'>comparison_workflow.yml</a>).
*  Workflow Steps:
    *  Step 1: Get repo contents: This step checks out the contents of the repository, making them available for subsequent steps.
    *  Step 2: Install dependencies: The necessary dependencies, including the ghapi and wandb Python packages, are installed to enable interaction with GitHub and wandb.
    *  Step 3: Parse value from the command: The body of the issue is parsed to extract the specified run ID for model comparison.
    *  Step 4: Generate the comparison report: If a run ID is found, this step generates the comparison report using the wandb API and reports functionality. The report is saved and its URL is stored as an output.
    *  Step 5: Make a comment with the GitHub API: If the comparison report is successfully generated, a comment is posted on the issue with a message and a link to the report.
*  wandb Script: The workflow invokes a Python script called <a href='generate_reports.py'>generate_reports.py</a>. This script utilizes the wandb API to interact with the Weights and Biases platform and generate the model comparison report. The script retrieves the baseline run based on specified project and tag, compares it with the user-specified run, and saves the comparison report.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Usage -->
## Usage

To utilize this CI/CD workflow for model comparison, follow these steps:

1.  Set up the Repository: Create a GitHub repository and clone it to your local machine. Set up the desired project structure, including model code, configuration files, and any other necessary resources.
2.  Configure Secrets: In the repository's GitHub settings, configure a secret named WANDB_API_KEY that stores your Weights and Biases API key. This secret will be used to authenticate and interact with the wandb platform.
3.  Define Specific Tag: Determine a specific tag that will be used to identify the run for comparison. It could be the baseline tag or dev tag or any desired tag. In this repo, we're using baseline tag.
4.  Update Workflow Configuration: In the .github/workflows directory of your repository, create or modify the given YAML file (e.g., comparison_workflow.yml) and copy the provided workflow configuration into it. Ensure that the WANDB_ENTITY, WANDB_PROJECT, and WANDB_TAG are set to the Github Actions Secrets.
5.  Add the Script File: Create a Python script (e.g., generate_reports.py) in your repository and copy the provided script code into it. This script handles the interaction with wandb, retrieves the baseline run, and generates the comparison report.
6.  Commit and Push: Commit the changes to the repository and push them to trigger the CI/CD workflow. The workflow will automatically execute whenever a new issue is created with the specified command in the body.
7.  Create Issues: Users can create issues (add issue types as desired) on the GitHub repository, specifying the command '/wandb <run_id>' in the issue body. Replace '<run_id>' with the actual ID of the model run to be compared.
8.  Review the Results: Once the workflow is executed, a comment will be posted on the issue with a message and a link to the generated comparison report. Users can review the report and analyze the performance of their model compared to the given specific tag.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Final Notes -->
## Final Notes

The CI/CD workflow implemented in this repository leverages the power of GitHub Actions and the wandb platform to automate the generation of model comparison reports. By integrating this workflow into your development and deployment process, one can streamline the evaluation of model performance and promote continuous improvement. The automated comparison reports facilitate collaboration, standardization, and communication, enabling to make informed decisions about your models.

The repository includes code originally contributed by <a href="https://github.com/hamelsmu">Hamel Husain</a>. The modifications made to the original code have enabled to tailor it to specific needs and enhance its functionality. Gratitude is extended to him for his initial work, which has significantly contributed to the creation of the code used in this repository. 

<p align="right">(<a href="#top">back to top</a>)</p>
