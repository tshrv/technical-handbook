"use client";

import { createContext, useState } from "react";

export const MyContext = createContext("MyContext Default Value");

export function MyProvider({ children }) {
  const [num, setNum] = useState(1231);
  return (
    <MyContext.Provider value={{ num, setNum }}>{children}</MyContext.Provider>
  );
}
