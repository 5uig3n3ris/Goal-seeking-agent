import streamlit as st
from grid import Grid
from agent import Agent

st.set_page_config(
    page_title="Goal-Seeking AI Agent",
    page_icon="🤖",
    layout="wide"
)

# Grid configuration
ROWS = 8
COLS = 8

START = (0, 0)
GOAL = (ROWS - 1, COLS - 1)

# Initialize session state
if "obstacles" not in st.session_state:
    st.session_state.obstacles = {
        (2, 2), (2, 3), (3, 3),
        (4, 1), (4, 2), (5, 5)
    }

if "path" not in st.session_state:
    st.session_state.path = None

if "step" not in st.session_state:
    st.session_state.step = 0

if "path_status" not in st.session_state:
    st.session_state.path_status = "not_searched"


# Environment
grid = Grid(
    ROWS,
    COLS,
    GOAL,
    st.session_state.obstacles
)

agent = Agent(START)


# Header
st.title("🤖 Goal-Seeking AI Agent")

st.write(
    "Build an environment, place obstacles, "
    "and watch an AI agent find its way to the goal."
)

st.divider()

# Instructions
st.markdown("""
If you're using a mobile phone, ensure you set it to desktop site mode 🖥
### How to play
- 🤖 Agent: Starting position
- 🎯 Goal: Destination
- 🧱 Obstacle: Blocks movement
- 🟦 Path: Route discovered by the agent

Click any empty cell to add or remove an obstacle.
""")

# Controls
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔍 Find Path", use_container_width=True):

        st.session_state.path = agent.find_path(
            START, GOAL, grid
        )

        st.session_state.step = 0

        if st.session_state.path is None:
            st.session_state.path_status = "unreachable"
        else:
            st.session_state.path_status = "found"

with col2:
    if st.button(
        "➡️ Next Step",
        use_container_width=True,
        disabled=not st.session_state.path
        or st.session_state.step >= len(st.session_state.path) - 1
    ):
        st.session_state.step += 1

with col3:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.obstacles = {
            (2, 2), (2, 3), (3, 3),
            (4, 1), (4, 2), (5, 5)
        }
        st.session_state.path = None
        st.session_state.step = 0
        st.session_state.path_status = "not_searched"

        st.rerun()


# Determine current agent position
path = st.session_state.path

if path:
    current_position = path[st.session_state.step]
else:
    current_position = START


# Display grid
st.subheader("Environment")

for row in range(ROWS):
    columns = st.columns(COLS)

    for col in range(COLS):
        position = (row, col)

        if position == current_position:
            symbol = "🤖"
        elif position == GOAL:
            symbol = "🎯"
        elif position in st.session_state.obstacles:
            symbol = "🧱"
        elif path and position in path:
            symbol = "🟦"
        else:
            symbol = "⬜"

        with columns[col]:
            if st.button(
                symbol,
                key=f"cell_{row}_{col}",
                use_container_width=True,
                disabled=position in (START, GOAL)
            ):
                if position in st.session_state.obstacles:
                    st.session_state.obstacles.remove(position)
                else:
                    st.session_state.obstacles.add(position)

                st.session_state.path = None
                st.session_state.step = 0
                st.session_state.path_status = "not_searched"

                st.rerun()


# Status information
st.divider()

if st.session_state.path_status == "unreachable":

    st.error(
        "🚫 No valid path found! "
        "The goal is unreachable with the current obstacles."
    )

    st.info(
        "Try removing some obstacles and searching again."
    )

elif st.session_state.path_status == "found":

    st.metric(
        "Shortest path length",
        len(path) - 1
    )

    st.progress(
        st.session_state.step / max(len(path) - 1, 1)
    )

    st.write(f"Agent position: {current_position}")

    if current_position == GOAL:
        st.success("🎉 Goal reached!")
    else:
        st.info(
            f"Step {st.session_state.step} "
            f"of {len(path) - 1}"
        )

else:

    st.info(
        "Waiting for instructions. Click Find Path to begin."
    )
