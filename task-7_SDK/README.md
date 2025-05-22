# 🧠 Task 07 – Understanding OpenAI Agents SDK

**Repo:** [01_ai_agents_first]
---

## ✅ 1. Why is the `Agent` class defined as a `@dataclass`?

The `Agent` class is defined as a **dataclass** to simplify and streamline the way data is stored and accessed.

- The `@dataclass` decorator in Python automatically generates boilerplate code like `__init__`, `__repr__`, and `__eq__` methods.
- This makes the class cleaner and more maintainable.
- Since the `Agent` class is mainly used to **store structured data** (like tools, instructions, models, etc.), using a dataclass is the most appropriate and efficient approach.

> 💡 In short, it helps avoid unnecessary manual code and focuses on the core functionality of the agent.

---

## ✅ 2a. Why is the system prompt stored as `instructions` inside the `Agent` class? Why can it also be a callable?

The system prompt — also known as `instructions` — tells the agent **how it should behave**, like:

> *“You are a helpful assistant that explains complex topics in simple language.”*

- `instructions` can be a **string** for simple static instructions.
- Or a **callable** (like a function) for dynamic instructions based on runtime context.

> 🔁 This allows the agent to adapt its behavior based on changing data or inputs.

---

## ✅ 2b. Why is the user prompt passed as a parameter in `Runner.run()` and why is this method a `classmethod`?

- The **user prompt** is passed during execution because it’s dynamic — it changes based on user input.
- The `run()` method is a `@classmethod`, which means:

  - It runs without needing to create a separate instance.
  - It offers a clean and simple way to invoke agent logic directly.

### Example:
```python
response = Runner.run("Write a poem about AI.")
⚙️ This makes the SDK easier and faster to work with for developers.

✅ 3. What is the purpose of the Runner class?
The Runner class acts as a controller or interface for managing agent logic. It handles:

Running the agent

Passing the user prompt and context

Returning the agent’s output

Think of it like a manager that sends instructions to the agent and fetches the response, hiding all the complexity underneath.

✅ 4. What are generics in Python? Why are they used for TContext?
Generics allow functions or classes to work with different data types in a type-safe way.

TContext is a type variable that tells Python:

"This can be any type — a string, a dictionary, or even a custom class."

It improves flexibility, reusability, and ensures proper type checking in code editors.

Example:
TContext = TypeVar("TContext")

class Runner(Generic[TContext]):
    ...
