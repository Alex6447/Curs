from src.utils.log_tools import logger
from src.task_1 import get_tool

# handler_id = logger.add("logs/log.log", level="DEBUG")
# logger.remove(handler_id)
# logger.add("logs/log.log", level="INFO")

def main():
    # task 1
    res = get_tool('write url path url url read csv')
    logger.info(f"task 1: {res=}")
    
    # task 2
    
    


if __name__ == "__main__":
    main()
