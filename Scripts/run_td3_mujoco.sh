#!/usr/bin/env bash

envs=(HalfCheetah-v3 Hopper-v3 Walker2d-v3 Ant-v3)
#envs=(Hopper-v3)
seeds=5
max_iter=1000
alg=TD3

for (( j = 1; j <= seeds; ++j )); do
    for (( i = 0; i < ${#envs[@]}; ++i )); do
        echo ============================================
        echo starting Env: ${envs[$i]} ----- Exp_id $j

        python -m PolicyGradient.${alg}.main --env_id ${envs[$i]} --max_iter ${max_iter} --model_path PolicyGradient/${alg}/trained_models --seed $j

        echo finishing Env: ${envs[$i]} ----- Exp_id $j
        echo ============================================
    done
done

