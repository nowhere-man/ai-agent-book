# Experiment 5-4: Paper to PPT

This lab compares two ways to generate a Slidev deck from a local Markdown
manuscript:

- **Dual agent**: a Proposer writes `slides.md`; a fresh Reviewer inspects the
  rendered PNG pages and returns structured feedback.
- **Single agent**: one conversation writes, renders, reviews, and revises the
  deck while its image history accumulates.

Both paths use the OpenAI API. The experiment records per-call token usage and
the peak prompt size so the context cost of the two designs can be compared.

## Quick start

From the repository root:

```bash
uv sync --locked --python 3.12 --extra ch5
source .venv/bin/activate
cd chapter5/paper-to-ppt
cp env.example .env
```

Set `OPENAI_API_KEY` in `.env`, then install the JavaScript renderer:

```bash
npm install
python demo.py --dry-run
```

`--dry-run` performs the complete render/review/revision loop without an API
call. To run the real comparison:

```bash
python demo.py --mode both --max-rounds 3
```

The default input is [`paper/sample_paper.md`](paper/sample_paper.md). Use a
different local Markdown file with `--paper PATH`. `--smoke` only checks the
Slidev renderer, while `--mode dual` and `--mode single` run one arm.

## Options

```text
--paper PATH          Local Markdown manuscript (default: paper/sample_paper.md)
--out-dir DIR         Evidence output directory (default: output/)
--text-model NAME     OpenAI text model (or TEXT_MODEL)
--vision-model NAME   OpenAI vision model (or VISION_MODEL)
--mode {both,dual,single}
--max-rounds N
--dry-run              Offline scripted loop; no key required
--smoke                Renderer-only check; no key required
```

The only credential is `OPENAI_API_KEY`. The script always calls the OpenAI
endpoint; there are no alternate provider, proxy, or remote manuscript paths.

## Files

| File | Purpose |
|---|---|
| `demo.py` | Command-line entry point and comparison orchestration |
| `agents.py` | Proposer, Reviewer, self-review agent, and token receipts |
| `renderer.py` | Slidev PNG rendering |
| `make_figures.py` | Generates the small local charts used by the demo |
| `paper/sample_paper.md` | Default local Markdown manuscript |
| `package.json` | Slidev and browser-rendering dependencies |

Each run writes `slides.md`, review JSON, token receipts, and rendered PNGs
under the selected output directory. PNGs are retained per page so layout
feedback can be reproduced.

## Design notes

The Proposer receives manuscript text and structured review text only. The
Reviewer receives the newest rendered PNG pages in a fresh request. The
single-agent arm intentionally keeps previous images in its conversation so
the context-growth difference is observable.

The source contract requires 18-20 pages, at most four Markdown bullets per
page, and bounded image layout. The Vision Reviewer remains the authority for
pixel-level readability and overflow; the offline reviewer only checks text
density.

## 中文说明

本实验将本地 Markdown 稿件生成 Slidev 演示文稿，并比较“双 Agent 提议者-审核者”和“单
Agent 自审”两种上下文组织方式。两种方式都只调用 OpenAI：配置 `OPENAI_API_KEY` 即可。

```bash
cd chapter5/paper-to-ppt
cp env.example .env
python demo.py --dry-run                 # 离线验证渲染和审查闭环
python demo.py --mode both --max-rounds 3 # 使用 OpenAI 运行完整对照
```

默认输入为 `paper/sample_paper.md`，可通过 `--paper` 指定其他本地 Markdown 文件。输出目录
包含每轮 `slides.md`、审查 JSON、token 收据和逐页 PNG。`--smoke` 只检查 Slidev 渲染链路。
