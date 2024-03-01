from prefect import flow, get_run_logger

@flow(name="Demo")
def basic_flow():
    logger = get_run_logger()
    logger.warning("The fun is about to begin")

if __name__ == "__main__":
    basic_flow()