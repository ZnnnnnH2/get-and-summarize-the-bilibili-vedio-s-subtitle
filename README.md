# get-and-summarize-the-bilibili-vedio-s-subtitle

# 获取并总结B站视频字幕

## brief intro

## 简要介绍

this is my small-tools set project1
 这是我的小工具集项目1

you can get the subtitle of bilibili vedio through BV or aid\cid, then summarize it using ai API.
 你可以通过BV号或aid\cid获取B站视频的字幕，然后使用AI API对字幕进行总结。

## how to use?

## 如何使用？

just run the app.py and follow the instructions in the terminal.
 只需运行 app.py 并按照终端中的指示操作即可。

## notes

## 注意事项

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

- 你需要在 header.json 或 raw_header 中填写你的请求头信息。

  - header.json 的内容应该如下所示：

    ```json
    {
      "User-Agent": "你的 User-Agent",
      "Cookie": "你的 Cookie"
    }
    ```

  - raw_header 的内容应该如下所示：

    ```
    User-Agent: 你的 User-Agent
    Cookie: 你的 Cookie
    ```

- finally, the subtitle will be saved in `subtitle.txt` and the summary will be saved in `summary.txt`.

- 最终，字幕会被保存在 `subtitle.txt` 文件中，总结内容会被保存在 `summary.txt` 文件中。

- you can change the prompt in the `app.py` to have a better use of ai api.

- 你可以修改 `app.py` 文件中的 prompt 以更好地使用 AI API。

## references

## 参考资料

- [BILIBILI 字幕提取教程简略版](https://www.cnblogs.com/apachecn/p/18415093)
- [Bilibili BV号获取AID和CID接口免费使用 - FreeJK免费API](https://freejk.com/api/24)
