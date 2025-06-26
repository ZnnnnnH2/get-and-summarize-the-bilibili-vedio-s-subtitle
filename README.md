# get-and-summarize-the-bilibili-vedio-s-subtitle

## brief intro
this is my small-tools set project1

you can get the subtitle of bilibili vedio through BV or aid\cid, then summarize it using ai API.

## how to use?

just run the app.py and follow the instructions in the terminal.

## notes

- you need to finish your headers in header.json or raw_header. 
  - Things in header.json should be like this:
    ```json
    {
      "User-Agent": "your user agent",
      "Cookie": "your cookie"
    }
    ```
  - Things in raw_header should be like this:
    ```
    User-Agent: your user agent
    Cookie: your cookie
    ```

- finally, the subtitle will be saved in `subtitle.txt` and the summary will be saved in `summary.txt`.
- you can change the prompt in the `app.py` to have a better use of ai api.

## references

- [BILIBILI 字幕提取教程简略版](https://www.cnblogs.com/apachecn/p/18415093)
- [Bilibili BV号获取AID和CID接口免费使用 - FreeJK免费API](https://freejk.com/api/24)
