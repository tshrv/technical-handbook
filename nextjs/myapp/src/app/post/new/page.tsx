"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

type Post = {
  id: number;
  userId: number;
  title: string;
  body: string;
};

export default function PostCreate() {
  const router = useRouter();
  const [title, setTitle] = useState<string>("");
  const [titleError, setTitleError] = useState<boolean>(false);
  const titleErrorMessage = "Title length should be less than 10";

  const [body, setBody] = useState<string>("");
  const [bodyError, setBodyError] = useState<boolean>(false);
  const bodyErrorMessage = "Body length should be less than 20";

  const formErrorMessage = "Please fix errors above";
  const [formError, setFormError] = useState<string | null>(null);

  const [newObject, setNewObject] = useState<Post>();

  useEffect(() => {
    console.log("title", title);
    if (title.length > 9) {
      setTitleError(true);
    } else {
      setTitleError(false);
    }
  }, [title]);

  useEffect(() => {
    console.log("body", body);
    if (body.length > 20) {
      setBodyError(true);
    } else {
      setBodyError(false);
    }
  }, [body]);

  const submitForm = () => {
    if (titleError || bodyError) {
      setFormError(formErrorMessage);
      return;
    }
    setFormError(null);
    fetch("https://jsonplaceholder.typicode.com/posts", {
      method: "POST",
      body: JSON.stringify({
        title: title,
        body: body,
        userId: 1,
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    })
      .then((response) => response.json())
      .then((json) => setNewObject(json));
  };
  return (
    <div className="flex flex-col gap-y-2">
      <h1>Create New Post</h1>
      <input
        type="text"
        name="title"
        onChange={(e) => setTitle(e.target.value)}
        placeholder="your title here"
      />
      {titleError && <span className="text-red-600">{titleErrorMessage}</span>}
      <input
        type="text"
        name="body"
        onChange={(e) => setBody(e.target.value)}
        placeholder="your body here"
      />
      {bodyError && <span className="text-red-600">{bodyErrorMessage}</span>}

      <button className="border border-black p-2" onClick={submitForm}>
        Submit
      </button>
      {formError && <span className="text-red-600">{formError}</span>}

      {newObject && (
        <div>
          <p>New Object</p>
          <p>#{newObject.id}</p>
          <p>{newObject.title}</p>
          <p>{newObject.body}</p>
        </div>
      )}
    </div>
  );
}
