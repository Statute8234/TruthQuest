# TruthQuest

This Python interactive game uses the Ursina game engine to ask and answer questions in a hot-seat format. Players take turns in the hot seat, answering pre-defined questions or adding their own. The game interface includes buttons for truth, truth, and QA, and a timer with a health bar. The game encourages social interaction and conversation among players, providing a simple yet engaging experience.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Imports](#Imports)
- [Rating: 6/10](#Rating)

# About

This Python project is an interactive game using the Ursina game engine. The game aims to encourage social interaction and conversation among players by asking and answering questions in a hot-seat style format. Players take turns being in the hot seat, with the option to answer truthfully or lie. The game features pre-defined questions and allows players to add their own questions. The interface includes buttons for answer options like "Lie," "Truth," and "QA," which players can interact with using mouse input. A timer feature, represented by a health bar, counts down the time remaining for the current player's turn. Overall, the project provides a simple yet engaging gameplay experience.

# Features

The Ursina Card Game is an interactive game using the Ursina game engine, featuring a hot-seat style format, pre-defined and custom questions, and answer options like lie, truth, and QA. Players take turns in the "hot seat" and can choose to answer truthfully or lie during their turn. The game also includes a timer feature (health bar) that adds urgency to the game, requiring quick decision-making. Despite its simplicity, the game provides an engaging and interactive experience, requiring players to think on their feet, strategize, and engage in conversation. The game offers a fun way to connect with others and test wit and creativity. Overall, the Ursina Card Game is a fun way to connect with others and test their wit and creativity.

# Imports

random, ursina, ursina.prefabs.health_bar

# Rating

The code for a turn-based game is functional, with player interaction through button clicks and input fields. Randomization adds variability to gameplay, and the code is divided into functions for improved readability. However, there are some cons, such as unclear variable names, use of magic numbers without explanation, overuse of global variables, code duplication, error handling for edge cases, and the absence of audio.
To improve, the code should be refactored to eliminate duplication and improve clarity, implement error handling for edge cases, and enhance the user interface with better layout and visual elements. Documentation should be added to explain the purpose of each function and section of code, and testing should be conducted under various scenarios to identify and fix bugs or usability issues.
Lastly, optimization should be made for performance, especially in the update loop, to ensure smooth gameplay even on lower-end devices. By addressing these issues, the code can be improved for a more engaging and enjoyable gaming experience.
