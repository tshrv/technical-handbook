"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

type Post = {
  id: number;
  userId: number;
  title: string;
  body: string;
};

// async function getPosts(url: string): Promise<Post[]> {
//   try {
//     const response = await fetch(url);
//     if (!response.ok) {
//       throw new Error("Network Error");
//     }
//     const data: Post[] = await response.json();
//     return data;
//   } catch (error) {
//     console.log(error);
//     throw error;
//   }
// }

export default function PostList() {
  const [data, setData] = useState<Post[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState(null);
  const router = useRouter();
  useEffect(() => {
    console.log("on mount only");
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((response) => {
        if (!response.ok) {
          throw new Error("API Error");
        }
        return response.json();
      })
      .then((data) => {
        setData(data);
        setIsLoading(false);
      })
      .catch((error) => {
        setError(error);
        setIsLoading(false);
      });
  }, []);

  if (isLoading) {
    return (
      <div>
        <p>Loading</p>
      </div>
    );
  }
  if (error) {
    return (
      <div>
        <p>(error)</p>
      </div>
    );
  }
  return (
    <div>
      <h1>Post List</h1>
      <div>
        {data.map((value, idx, arr) => {
          return (
            <p className="mb-2">
              #{value.id} {value.title}
              <button
                onClick={() => {
                  router.push(`/post/${value.id}`);
                }}
                className="border border-black p-2 m-2"
              >
                View
              </button>
            </p>
          );
        })}
      </div>
    </div>
  );
}
