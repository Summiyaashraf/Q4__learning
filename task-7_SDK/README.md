🧠 Task 07 – Understanding OpenAI Agents SDK
Repo: 01_ai_agents_first

✅ 1. Why is the Agent class defined as a @dataclass?
The Agent class is defined as a dataclass to simplify and streamline the way data is stored and accessed.

The @dataclass decorator in Python automatically generates boilerplate code like __init__, __repr__, and __eq__ methods.

This makes the class cleaner and more maintainable.

Since the Agent class is mainly used to store structured data (like tools, instructions, models, etc.), using a dataclass is the most appropriate and efficient approach.

In short, it helps avoid unnecessary manual code and focuses on the core functionality of the agent.

✅ 2a. Why is the system prompt stored as instructions inside the Agent class? Why can it also be a callable?
The system prompt — also known as instructions — is an important part of the agent’s setup. It tells the agent how it should behave, like:
“You are a helpful assistant that explains complex topics in simple language.”

instructions can be a string for simple static instructions.

Or a callable (like a function) when you need dynamic instructions generated at runtime — for example, based on context or user input.

Allowing instructions to be callable adds flexibility to the agent and enables it to behave differently depending on the situation.

✅ 2b. Why is the user prompt passed as a parameter in Runner.run() and why is this method a classmethod?
In the OpenAI Agents SDK:

The user prompt (the actual message or task) is passed to the agent during execution, which is why it’s a parameter in the run() method.

The run() method is a @classmethod, meaning it can be called on the class itself without creating an instance.

This design allows developers to run agents directly using the class, simplifying usage and making it easier to scale or integrate into other tools.

Example:
response = Runner.run("Write a poem about AI.")
This makes the SDK intuitive and easy to use for developers.

✅ 3. What is the purpose of the Runner class?
The Runner class acts as a controller or interface that handles:

Initializing and running the agent

Passing prompts and context

Managing execution flow and returning the agent’s output

Think of the Runner as a helper or manager that wraps around the Agent and abstracts away the complexity, so developers can focus on input/output without worrying about the internal setup.

✅ 4. What are generics in Python? Why are they used for TContext?
Generics in Python (introduced via typing) are used to create reusable code that works with multiple data types.

TContext is a type variable — it allows the developer to define what kind of data the context will hold.

This makes the SDK more type-safe and flexible.

For example:
TContext = TypeVar("TContext")
class Runner(Generic[TContext]):
    ...
Now, Runner can work with any context type (like str, dict, or even custom classes) while maintaining type checking and auto-completion support in editors like VS Code.

BY_SUMMIYA ASHRAF
