#!/usr/bin/env bash

#envs=(HalfCheetah-v3 Hopper-v3 Walker2d-v3 Swimmer-v3 Ant-v3 BipedalWalker-v2)
envs=(BipedalWalker-v2)
seeds=1
max_iter=1000
for (( i = 0; i < ${#envs[@]}; ++i )); do
      for (( j = 1; j <= seeds; ++j )); do
          echo ============================================
          echo starting Env: ${envs[$i]} ----- Exp_id $j

          python -m PolicyGradient.DDPG.main --env_id ${envs[$i]} --max_iter ${max_iter} --model_path PolicyGradient/DDPG/trained_models --seed $j

          echo finishing Env: ${envs[$i]} ----- Exp_id $j
          echo ============================================
      done
done

