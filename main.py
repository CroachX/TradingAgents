from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

import logging
import langchain

# Configure logging to write to a file
# This will create 'langchain_debug.log' in the directory from which the script is run.
logging.basicConfig(filename='langchain_debug.log',
                    filemode='w',  # 'w' for overwrite, 'a' for append
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Enable Langchain's verbose debug mode - it will now use the configured logger
langchain.debug = True

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["deep_think_llm_gemini"] = "gemini-1.0-pro"  # Use a different model
config["quick_think_llm_gemini"] = "gemini-1.5-flash-latest"  # Use a different model
config["max_debate_rounds"] = 1  # Increase debate rounds
config["online_tools"] = True  # Increase debate rounds

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
