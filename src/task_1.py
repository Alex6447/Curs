from utils.log_tools import logger

def get_tool(text: str):
    
	tool = {
		"calc":["sum", "add", "plus", "minus", "multiply", "divide", "math"],
		"web": ["http", "https", "url", "link", "search", "web"],
		"db": ["sql", "select", "table", "join", "query", "database"],
		"fs": ["file", "csv", "json", "read", "write", "path"]
	}  

	keys = {}
	for key, value in tool.items():
		logger.debug(f"{key=}; {value=} ")
		count = 0
		for v in value:
			logger.debug(f"{v=}")
			count += text.lower().count(v)
		keys[key] = count
	return max(keys, key=keys.get)

if __name__ == "__main__":
	res = get_tool('write url path url url read csv')
	logger.info(f"{res=}")