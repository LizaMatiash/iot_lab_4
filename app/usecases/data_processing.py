from ..entities.agent_data import AgentData
from ..entities.processed_agent_data import ProcessedAgentData


def process_agent_data(agent_data: AgentData) -> ProcessedAgentData:

    value = agent_data.accelerometer.z

    if value < 0:
        road_state = "false"
    elif value > 15000:
        road_state = "false"
    else:
        road_state = "true"

    processed_data_batch = ProcessedAgentData(
        road_state=road_state,
        agent_data=agent_data
    )

    return processed_data_batch
