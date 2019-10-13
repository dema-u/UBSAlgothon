import stats

import gym
import pandas as pd
import numpy as np

class BondFuturesTradingEnv(gym.Env):

    metadata = {'render.modes': ['human']}

    def __init__(self, validation=False, trade_cost_percentage=0.02):

        float_range = np.finfo('float32').min, np.finfo('float32').max

        self.observation_space = gym.spaces.Box(*float_range, shape=(27,), dtype=np.float32)
        self.action_space = gym.spaces.Box(-1, 1, [3], dtype=np.float32)

        self.features = np.load('rl_env/data/features.npy')
        self.returns = np.load('rl_env/data/returns.npy')

        self.start_index = 456 if validation else 0
        self.end_index = 570 if validation else 456

        self.done = False
        self.exposures = np.array([0.0, 0.0, 0.0])
        self.trade_cost_percentage = trade_cost_percentage
        self.portfolio_returns = [3]

    def get_observation(self):

        features = self.features[self.index].tolist()
        exposures = self.exposures.tolist()

        observation = np.array(features + exposures)

        return observation

    def step(self, exposures):

        total_traded = abs(exposures - self.exposures)

        self.exposures = exposures
        self.index += 1

        reward = sum(self.exposures*self.returns[self.index]) - sum(total_traded*self.trade_cost_percentage)

        self.portfolio_returns.append(reward)
        observation = self.get_observation()

        done = True if (self.index == self.end_index-1) else False

        return observation, reward, done, {}


    def reset(self):

        self.done = False
        self.index = self.start_index
        self.exposures = np.array([0.0, 0.0, 0.0])
        self.portfolio_returns = [3]

        observation = self.get_observation()

        return observation

    def render(self, mode='human'):
        series = np.array(self.portfolio_returns).cumsum()
        stats.print_full_statistics(series)