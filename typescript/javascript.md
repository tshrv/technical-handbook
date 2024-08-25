## var, let and const

- var: Function-scoped, can be re-declared and hoisted with undefined.
- let: Block-scoped, cannot be re-declared within the same scope, hoisted without initialization.
- const: Block-scoped, cannot be re-declared or reassigned, hoisted without initialization, but properties of objects it holds can be modified.

Choosing between them:

- Use let for variables that need to be reassigned.
- Use const for variables that should not be reassigned.
- Avoid using var to prevent issues related to scope and hoisting.

## Hoisting

### `var` Hoisting

Variables declared with var are hoisted to the top of their function or global scope and are initialized with undefined. This means you can reference them before their declaration, but they will have the value undefined until the assignment is executed.

### `let` and `const` Hoisting

Variables declared with let and const are also hoisted to the top of their block scope, but they are not initialized. Accessing them before their declaration will result in a ReferenceError.

### Function Hoisting

Function declarations are hoisted to the top of their scope and are fully initialized. This means you can call the function before its declaration.

## Currying

Currying is a functional programming technique where a function is transformed into a sequence of functions, each taking a single argument. In JavaScript, this can be useful for creating more flexible and reusable functions. Here's an example to illustrate currying in JavaScript:

```js
function add(a, b, c) {
  return a + b + c;
}
```

With currying, you can transform this function into a series of functions that each take one argument:

```js
function curriedAdd(a) {
  return function (b) {
    return function (c) {
      return a + b + c;
    };
  };
}

// Usage:
console.log(curriedAdd(1)(2)(3)); // Output: 6
```

Using arrow functions

```js
const curriedAdd = (a) => (b) => (c) => a + b + c;

// Usage:
console.log(curriedAdd(1)(2)(3)); // Output: 6
```

## Closure

In JavaScript, a closure is a feature where an inner function has access to the outer (enclosing) function’s variables and parameters, even after the outer function has returned. Closures are created every time a function is created, at function creation time.
Key Aspects of Closures

- Local Variables: The inner function has access to the outer function’s variables.
- Global Variables: The inner function has access to global variables.
- Own Variables: The inner function has access to its own variables.

```js
function createPerson(name) {
  let age = 0;

  return {
    getName: function () {
      return name;
    },
    getAge: function () {
      return age;
    },
    growOlder: function () {
      age += 1;
    },
  };
}

const person = createPerson("John");
console.log(person.getName()); // Output: 'John'
console.log(person.getAge()); // Output: 0
person.growOlder();
console.log(person.getAge()); // Output: 1
```

## Prototypes

The Basics of Prototypes

- Prototype Chain: When you try to access a property or method on an object, JavaScript will first look for that property or method on the object itself. If it is not found, JavaScript will then look for it on the object's prototype, and then on the prototype's prototype, and so on, until it reaches Object.prototype, which is the top-level prototype object. This is known as the prototype chain.

- Prototype Property: Functions in JavaScript have a special property called prototype, which is used to build the prototype chain. When a function is used as a constructor with the new keyword, the new object’s prototype is set to the constructor function’s prototype property.

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.sayHello = function () {
  console.log(`Hello, my name is ${this.name}`);
};

const alice = new Person("Alice", 30);
alice.sayHello(); // Output: Hello, my name is Alice

console.log(alice.hasOwnProperty("name")); // Output: true
console.log(alice.hasOwnProperty("sayHello")); // Output: false
console.log(alice.__proto__.hasOwnProperty("sayHello")); // Output: true
```

Modern Approach: Class Syntax

Since ES6, JavaScript has introduced class syntax as a more familiar way to create objects and deal with inheritance. Under the hood, it still uses prototypes:

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHello() {
    console.log(`Hello, my name is ${this.name}`);
  }
}

class Employee extends Person {
  constructor(name, age, jobTitle) {
    super(name, age);
    this.jobTitle = jobTitle;
  }

  sayJob() {
    console.log(`My job title is ${this.jobTitle}`);
  }
}

const charlie = new Employee("Charlie", 28, "Manager");
charlie.sayHello(); // Output: Hello, my name is Charlie
charlie.sayJob(); // Output: My job title is Manager
```

This class syntax is syntactic sugar over the prototypal inheritance and makes the code more readable and familiar for developers coming from other object-oriented languages.
Conclusion

Prototypes are a powerful feature of JavaScript that allow for property and method sharing across objects. Understanding how prototypes and the prototype chain work is essential for mastering JavaScript inheritance and writing efficient, reusable code. The introduction of the class syntax in ES6 provides a cleaner way to work with prototypes while maintaining backward compatibility with the existing prototypal inheritance system.

## Promise

Here's a basic example of using JavaScript promises. A promise in JavaScript is an object representing the eventual completion or failure of an asynchronous operation.

```js
// Create a new promise
let myPromise = new Promise((resolve, reject) => {
  let success = true; // Change this to false to see the reject case

  if (success) {
    resolve("Promise was successful!");
  } else {
    reject("Promise was rejected.");
  }
});

// Handle the promise
myPromise
  .then((message) => {
    console.log(message); // "Promise was successful!"
  })
  .catch((error) => {
    console.log(error); // "Promise was rejected."
  });
```

`Promise.all` allows you to wait for multiple promises to resolve:

```js
let promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Promise 1 resolved");
  }, 1000);
});

let promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Promise 2 resolved");
  }, 2000);
});

let promise3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Promise 3 resolved");
  }, 3000);
});

Promise.all([promise1, promise2, promise3])
  .then((messages) => {
    console.log(messages); // ["Promise 1 resolved", "Promise 2 resolved", "Promise 3 resolved"] after 3 seconds
  })
  .catch((error) => {
    console.log(error);
  });
```
