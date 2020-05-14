#!/usr/bin/env python
# Created at 2020/5/14
import multiprocessing

import click
import yaml

GAIL_TEMPLATE = "python -m Algorithms.{0}.{1}.main --env_id {2} --save_model_path {3} " \
                "--num_process {4}  --render {5} --config_path {6} --expert_data_path {7}"

PPO_TEMPLATE = "python -m Algorithms.{0}.{1}.main --env_id {2} --max_iter 500 --model_path {3} --num_process {4}" \
               "--render {5}"


@click.command()
@click.option("--version", type=click.Choice(['pytorch', 'tf2']), default="pytorch", help="Version of implementation")
@click.option("--algo", type=str, default="PPO", help="Version of implementation")
@click.option("--envs", type=str, default="HalfCheetah-v3,Hopper-v3,Walker2d-v3,Swimmer-v3,Ant-v3",
              help="Environment ids")
def generate(version, algo, envs):
    click.echo(f"Version: {version}, Algorithm: {algo}, Envs: {envs}")

    envs_list = envs.split(",")
    config_dict = {
        "session_name": f"run-all-{algo}",
        "start_directory": f"~/PycharmProjects/DeepRL_Algorithms",
        "windows": []
    }

    panes_list = []
    for env in envs_list:
        print(f"Generate config for env : {env}")

        run_command = None
        tensor_board_command = f"tensorboard --logdir=./{version}/log"  # run tensorboard for visualization
        if algo == "GAIL":
            run_command = GAIL_TEMPLATE.format(version,
                                               algo,
                                               env,
                                               f"./{version}/{algo}/trained_models",
                                               int(multiprocessing.cpu_count() / 2),
                                               False,
                                               f"./{version}/{algo}/config/config.yml",
                                               f"./{version}/{algo}/data/{env}.npz")
            tensor_board_command = f"tensorboard --logdir=./{version}/{algo}/log"  # run tensorboard for visualization

        elif algo == "PPO":
            run_command = PPO_TEMPLATE.format(version,
                                              algo,
                                              env,
                                              f"./{version}/{algo}/trained_models",
                                              int(multiprocessing.cpu_count() / 2),
                                              False)

        panes_list.append(run_command)
        panes_list.append(tensor_board_command)

    config_dict["windows"].append({
        "window_name": f"{algo}",
        "panes": panes_list,
        "layout": "tiled"
    })

    yaml.dump(config_dict, open(f"run_all_{algo}.yaml", "w"), default_flow_style=False)


if __name__ == '__main__':
    generate()
