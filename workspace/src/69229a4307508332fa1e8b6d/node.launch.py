import json
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    parameters = json.loads('{"joint_ids":["6922930007508332fa1e8b16"],"control_mode":"position","max_velocity":10}')
    configuration = json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')
    inbound_connections = json.loads('[]')
    outbound_connections = json.loads('[]')
    env = {
        "POLYFLOW_NODE_ID": "69229a4307508332fa1e8b6d",
        "POLYFLOW_PARAMETERS": json.dumps(parameters),
        "POLYFLOW_CONFIGURATION": json.dumps(configuration),
        "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(inbound_connections),
        "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(outbound_connections),
    }

    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["python3", "workspace/src/69229a4307508332fa1e8b6d/odrive-s1/node.py"],
                additional_env=env,
                output="screen",
            )
        ]
    )