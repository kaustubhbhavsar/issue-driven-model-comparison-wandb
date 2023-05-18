import os, wandb
import wandb.apis.reports as wr

assert os.getenv('WANDB_API_KEY'), 'You must set the WANDB_API_KEY environment variable'

def get_baseline_run(
  entity: str, 
  project: str, 
  tag: str
):
    """
    The function get_baseline_run retrieves the baseline run from a project using tags.

    Parameters:   
        entity (str): The entity name. 
        project (str): The project name. 
        tag (str): The baseline tag. 
    
    Returns:
        wandb.apis.public.Run: The baseline run.
     
    Raises:
        AssertionError: If there is not exactly one run with the specified tag "baseline".
    """
    api = wandb.Api()
    runs=api.runs(f'{entity}/{project}', {"tags": {"$in": [tag]}})
    assert len(runs) == 1, 'There must be exactly one run with the tag "baseline"'
    return runs[0]

def compare_runs(
  entity: str = None,
  project: str = None,
  tag: str = None,
  run_id: str = None
):
    """
    The function compare_runs compares two runs and generates a report.
    
    Parameters:
        entity (str): The entity name. If not provided, it defaults to the value of the 'WANDB_ENTITY' environment variable.
        project (str): The project name. If not provided, it defaults to the value of the 'WANDB_PROJECT' environment variable.
        tag (str): The baseline tag. If not provided, it defaults to the value of the 'BASELINE_TAG' environment variable.
        run_id (str): The ID of the current run. If not provided, it defaults to the value of the 'RUN_ID' environment variable.
    
    Returns:
        str: The URL of the generated report.
        
    Raises:
         AssertionError: If the 'RUN_ID' environment variable or the run_id argument is not set.
    """
    entity = os.getenv('WANDB_ENTITY') or entity
    project = os.getenv('WANDB_PROJECT') or project
    tag = os.getenv('BASELINE_TAG') or tag
    run_id = os.getenv('RUN_ID') or run_id
    assert run_id, 'You must set the RUN_ID environment variable or pass a `run_id` argument'

    baseline = get_baseline_run(entity=entity, project=project, tag=tag)
    report = wr.Report(entity=entity, 
                       project=project,
                       title='Compare Runs',
                       description=f"A comparison of runs, the baseline run name is {baseline.name}") 

    pg = wr.PanelGrid(
        runsets=[wr.Runset(entity, project, "Run Comparison").set_filters_with_python_expr(f"ID in ['{run_id}', '{baseline.id}']")],
        panels=[wr.RunComparer(diff_only='split', layout={'w': 24, 'h': 15}),]
    )
    report.blocks = report.blocks[:1] + [pg] + report.blocks[1:]
    report.save()

    if os.getenv('CI'): # is set to `true` in GitHub Actions https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f: # write the output variable REPORT_URL to the GITHUB_OUTPUT file
            print(f'REPORT_URL={report.url}', file=f)
    return report.url

if __name__ == '__main__':
    print(f'The comparison report can found at: {compare_runs()}')
