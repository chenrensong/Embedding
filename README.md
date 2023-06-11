# README.md

## Embedding

This application, based on InstructorEmbedding and FastAPI, simulates the input and output of OpenAI's embeddings interface. It implements the ability to handle text-to-vector conversion locally.

---

## Getting Started

First, make sure you have installed Python 3.7 or a later version. You can set up and run the project following these steps:

1. Clone this repository:

    ```
    git clone https://github.com/chenrensong/embedding.git
    ```

2. Navigate into the project folder:

    ```
    cd embedding
    ```

3. Build the docker image:

    ```
    docker build -t embedding .
    ```

4. Run the application:

    ```
    docker run -t -p 8000:80 embedding 
    ```

    Now, your application should be running and can be checked by visiting `http://localhost:8000`.

---

## API Interface

### GET `/`

Returns a welcome message.

### POST `/embeddings`

Accepts a JSON object of `EmbeddingRequest` and returns an `EmbeddingResponse` object, which includes the embeddings of the requested text.

Example requests:

```crul
curl http://127.0.0.1:8000/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Your text string goes here",
    "model": "text2vec-base-chinese"
  }'
```

Example response:
```json
{
  "data": [
    {
      "embedding": [
        -0.006929283495992422,
        -0.005336422007530928,
        -4.547132266452536e-05,
        -0.024047505110502243
      ],
      "index": 0,
      "object": "embedding"
    }
  ],
  "model": "text2vec-base-chinese",
  "object": "list",
  "usage": {
    "prompt_tokens": 5,
    "total_tokens": 5
  }
}
```

CSharp Request example:

```CSharp
HttpClient client = new HttpClient();
var request = new {
    input = "Hello, I'm Chen Rensong",
    instruction = "Represent the query for retrieval"
};
var json = JsonSerializer.Serialize(request);
var data = new StringContent(json, Encoding.UTF8, "application/json");
HttpResponseMessage response = await client.PostAsync("http://127.0.0.1:8000/embeddings", data);
string result = await response.Content.ReadAsStringAsync();
Console.WriteLine(result);
```

---

## Contribution

Feel free to submit an Issue or Pull Request to improve the project. Please ensure that your code follows the PEP8 coding style and that tests have been performed before submitting the Pull Request.

---

## License

This project is licensed under the MIT License.
---

## Contact

If you have any questions or suggestions, feel free to contact me at chenrensong@outlook.com.

---

## Acknowledgements

Thanks to OpenAI for the inspiration that made this project possible.
