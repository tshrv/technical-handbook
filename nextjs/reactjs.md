## Hooks

### Use State, Use Memo

```js
import { React, useState, useMemo } from "react";

export function App(props) {
  const [id, setId] = useState(0);
  const [num, setNum] = useState(0);
  return (
    <div className="App">
      <h1>Hello React.{id}</h1>
      <button onClick={() => setId(id + 1)}>UpdateId</button>
      <h2>Start editing to see some magic happen!</h2>
      <ExpComp num={num} />
      <button onClick={() => setNum(num + 1)}>Increment</button>
      <button onClick={() => setNum(num - 1)}>Decrement</button>
      <button onClick={() => setNum(num)}>Update same</button>
    </div>
  );
}

// Log to console
console.log("Hello console");

function ExpComp(props) {
  function expComp(num) {
    console.log("expComp");
    return num + 1;
  }
  let num = props.num;
  // const result = useMemo(() => expComp(num), [num])
  const result = expComp(num);
  return (
    <div>
      <p>Num: {num}</p>
      <p>Result: {result}</p>
    </div>
  );
}
```
