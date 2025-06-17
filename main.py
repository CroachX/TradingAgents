from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

import logging
import langchain

# Configure basicConfig for root logger
# Set root to INFO to reduce verbosity from other libraries if they are too noisy at DEBUG
logging.basicConfig(filename='langchain_debug.log',
                    filemode='w',  # 'w' for overwrite
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Get the Langchain logger and set its level to DEBUG
# This ensures Langchain's specific debug messages are captured.
langchain_logger = logging.getLogger('langchain')
langchain_logger.setLevel(logging.DEBUG)

# By default, child loggers (like 'langchain') propagate to root.
# If basicConfig added a handler to root, langchain_logger will use it.
# No need to add separate handlers unless specific formatting or multiple files are needed for langchain logs.

# Enable Langchain's verbose debug mode - it will use the 'langchain' logger we configured.
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
