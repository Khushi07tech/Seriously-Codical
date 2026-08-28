# ⚡ 𝓢𝓮𝓻𝓲𝓸𝓾𝓼𝓵𝔂-𝓒𝓸𝓭𝓲𝓬𝓪𝓵
> An upgraded Python workspace featuring my **Logic Lab**, refactored modular software architecture, desktop GUIs, and interactive utilities.

**Author:** ✧･ﾟ: * ✨ <font color="#9b62ad">𝑲𝒉𝒖𝒔𝒉𝒃𝒂𝒌𝒉𝒕 𝑰𝒓𝒇𝒂𝒏</font> ✨ *:･ﾟ✧

> ❝ Building strong fundamentals in programming by solving meaningful problems and gradually improving their efficiency and structure. ❞

> 💡 **Repo Note:** 
> A personal Python repository where I practice problem-solving, algorithmic thinking, and core DSA patterns. This workspace organizes my practice scripts into a structured `/src` package and refactors early code into cleaner, modular versions.

---

## 🎯 Purpose & Progression Approach

The primary goal of this repository is to:
* **Strengthen logical thinking** using Python.
* **Understand Data Structures and Algorithms (DSA)** from the ground up.
* **Transition from brute-force to optimized solutions** step-by-step.
* **Build consistency** in coding practice and document my learning journey in a structured way.

---

## 🔬 The Logic Lab (Problem-Solving & Patterns)

The repository is organized by problem-solving patterns rather than random topics. Inside `/src/logic_lab/`, I implement foundational algorithms and problem sets from scratch:

<table align="center">
  <tr>
    <th align="center">Module</th>
    <th align="center">Core Focus & Exercises</th>
  </tr>
  <tr>
    <td><b><code>01_basic_patterns</code></b></td>
    <td>Simple condition-based logic, nested loops, and star pattern printing</td>
  </tr>
  <tr>
    <td><b><code>02_array_logic</code></b></td>
    <td>Iteration, value tracking, frequency counting, and in-place list mutations</td>
  </tr>
  <tr>
    <td><b><code>03_math_algorithms</code></b></td>
    <td>Mathematical optimization, prime checking, and digit parsing</td>
  </tr>
  <tr>
    <td><b><code>04_two_pointers</code></b></td>
    <td>Array bounds convergence, palindrome checks, and list reversals</td>
  </tr>
  <tr>
    <td><b><code>05_sorting</code></b></td>
    <td>Manual sorting mechanics (Bubble, Insertion, and Selection Sort)</td>
  </tr>
  <tr>
    <td><b><code>06_binary_search</code></b></td>
    <td>Logarithmic index lookups and boundary occurrence tracking</td>
  </tr>
  <tr>
    <td><b><code>08_recursion</code></b></td>
    <td>Call-stack tracking, factorials, countdowns, and string reductions</td>
  </tr>
  <tr>
    <td><b><code>09_recursion_advanced</code></b></td>
    <td>Recursive binary search and dynamic Fibonacci sequences</td>
  </tr>
  <tr>
    <td><b><code>10_divide_and_conquer</code></b></td>
    <td>Merge Sort implementation and array partitioning steps</td>
  </tr>
  <tr>
    <td><b><code>11_backtracking</code></b></td>
    <td>State-space exploration and recursive subset generation</td>
  </tr>
</table>

---

## 🛠️ Modular Architecture (`/src`)

Beyond standalone problem-solving, this repository refactors my scripts into modular Python packages with clean `__init__.py` initializations:

<details>
  <summary><b>📱 Desktop Applications (<code>/src/apps</code>)</b></summary>
  <br>
  <ul>
    <li><b>Clock Suite:</b> Multi-screen PyQt5 clock, alarm, and stopwatch app.</li>
    <li><b>Library Manager:</b> Object-oriented catalog tracking system.</li>
    <li><b>Inventory Manager:</b> CSV-backed data persistence system for stock updates.</li>
    <li><b>Weather GUI:</b> Desktop weather app pulling live API data.</li>
  </ul>
</details>

<details>
  <summary><b>🎮 Interactive Games (<code>/src/games</code>)</b></summary>
  <br>
  <ul>
    <li><b>Hangman:</b> Word guessing game with visual state progression.</li>
    <li><b>RPSLS:</b> Rock-Paper-Scissors-Lizard-Spock modular game logic.</li>
  </ul>
</details>

<details>
  <summary><b>⚙️ Utilities Core (<code>/src/utils</code>)</b></summary>
  <br>
  <ul>
    <li><b>Calculator:</b> Order-of-operations parsing engine.</li>
    <li><b>Login System:</b> User authentication script.</li>
    <li><b>Temp Converter:</b> Unit conversion utility module.</li>
  </ul>
</details>

---

## Setup instructions:
1. **Clone the repo:** `git clone https://github.com/Khushi07tech/Seriously_Codical.git`
2. **Install requirements:** `pip install -r requirements.txt`
3. **Run any app:** `python src/logic_lab`

---
## Roadmap & Future Goals
- [x] **Modular Package Design:** Re-architected flat scripts into a professional `/src` package using `__init__.py` modules.
- [x] **Algorithmic Foundations:** Mastered Two-Pointers, Binary Search, and manual sorting algorithms (Bubble, Selection, Insertion).
- [x] **Recursive Logic:** Implemented call-stack mechanics, recursive string processing, and Merge Sort (Divide & Conquer).
- [x] **Complexity Analysis:** Embedded Big-O time and space complexity annotations across Logic Lab scripts.
- [ ] **Data Structure Deep-Dive:** Implement custom Stacks, Queues, Linked Lists, and Binary Search Trees in Python.
- [ ] **Intermediate Graph Algorithms:** Explore Breadth-First Search (BFS) and Depth-First Search (DFS) patterns.
- [ ] **Automated Testing:** Add unit tests using `pytest` to validate Logic Lab algorithms automatically.
