"use client";
import { useRouter, usePathname, useSearchParams } from "next/navigation";
import { MyContext } from "@/lib/provider";
import { useContext } from "react";

export default function About() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const { num, setNum } = useContext(MyContext);

  console.log("pathname", pathname);
  console.log("searchParams", searchParams);
  console.log("searchParams", searchParams.get("name"));
  return (
    <div>
      <button onClick={() => router.push("/")} className="text-blue-500">
        Home
      </button>
      <p>About me</p>
      <p>Value: {num}</p>
      <button onClick={() => setNum(num + 1)}>About.increase</button>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Sed, nobis.
        Velit, eos! Eos, fugit, repellat perspiciatis labore quos possimus totam
        minus dignissimos rem nesciunt consequuntur dolor corrupti neque aliquam
        laborum?
      </p>
    </div>
  );
}
