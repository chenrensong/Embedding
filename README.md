# Embedding

This application, based on InstructorEmbedding and FastAPI, simulates the input and output of OpenAI's embeddings interface. It implements the ability to handle text-to-vector conversion locally.

---

# Getting Started

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

# API Interface

## GET `/`

Returns a welcome message.

## POST `/embeddings`

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

# Model Download


## First Install Git LFS

### Windows

1. First, download the latest Git LFS Windows installer from the Git LFS GitHub repository page. The URL for the page is: https://github.com/git-lfs/git-lfs/releases/latest.

2. After downloading the `.exe` file, double-click on it to launch the installer.

3. The installer will guide you through the installation of Git LFS. The default settings should be fine, just click "Next" until the installation is complete.

4. After the installation, open a command prompt (either cmd or PowerShell) and type in the following command to make Git LFS available across all your repositories:

    ```
    git lfs install
    ```

By now, Git LFS should be successfully installed on your Windows machine.

### Mac

On a Mac, we'll use Homebrew to install Git LFS. If you haven't installed Homebrew yet, you can get the installation guide from its official website: https://brew.sh/

1. Open a terminal window.

2. If you have already installed Homebrew, just run the following command to install Git LFS:

    ```
    brew install git-lfs
    ```

3. After the installation, run the following command to make Git LFS available across all your repositories:

    ```
    git lfs install
    ```

By now, Git LFS should be successfully installed on your Mac machine.

And that's the steps for installing Git LFS on Windows and Mac. I hope this helps! If you encounter any issues during the installation, feel free to ask me.


## Second Clone Model


```Shell
cd Model
```

```Shell
git clone https://huggingface.co/shibing624/text2vec-base-chinese/tree/main
```

---

# Contribution

Feel free to submit an Issue or Pull Request to improve the project. Please ensure that your code follows the PEP8 coding style and that tests have been performed before submitting the Pull Request.

---

# License

This project is licensed under the MIT License.

---

# Contact

If you have any questions or suggestions, feel free to contact me at chenrensong@outlook.com.

---

# Acknowledgements

Thanks to OpenAI for the inspiration that made this project possible.
