from swarmy.agent import Agent
import random
import pygame


class MyAgent(Agent):
    def __init__(self, environment, controller, sensors, config):
        super().__init__(environment, controller, sensors, config)

        self.trajectory = []

    def initial_position(self):
        """
        Choose a random spawn that does not overlap a wall, obstacle, or
        previously placed agent.
        """
        # Match the 30x30 agent bounds used by Experiment for collision checks.
        half_size = 15
        world_width = self.config['world_width']
        world_height = self.config['world_height']
        static_rectangles = [item[1] for item in self.environment.get_static_rectangle_list()]
        placed_agents = getattr(self.environment, 'agent_list', [])

        # Fail clearly if the arena is too crowded instead of retrying forever.
        for _ in range(10000):
            x = random.randint(half_size, world_width - half_size)
            y = random.randint(half_size, world_height - half_size)
            candidate = pygame.Rect(x - half_size, y - half_size, 2 * half_size, 2 * half_size)

            overlaps_wall_or_obstacle = any(candidate.colliderect(rect) for rect in static_rectangles)
            overlaps_agent = any(
                candidate.colliderect(
                    pygame.Rect(
                        int(agent.actuation.position[0] - half_size),
                        int(agent.actuation.position[1] - half_size),
                        2 * half_size,
                        2 * half_size,
                    )
                )
                for agent in placed_agents
            )

            if not overlaps_wall_or_obstacle and not overlaps_agent:
                self.set_position(x, y, random.randint(0, 359))
                return

        raise RuntimeError(
            'Could not find a free spawn position after 10000 attempts. '
            'Reduce the number of agents or obstacles, or increase the arena size.'
        )

    def save_information(self, save_image):
        """
        Save information of the agent, e.g. trajectory or the environmental plot.
        save_image is True only for the last agent, so the shared image is saved once after all agents have drawn on it.
        Hint:
        - Use pygame.draw.lines() to draw the trajectory of the robot and access the surface of the environment with self.environment.display_surface
        - pygame allows to save an image of the current environment
        """
        print('Save information not implemented, check my_agent.py')
        """ your implementation here """
