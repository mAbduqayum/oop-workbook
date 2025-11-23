# Python Telegram Bot Exercises

## Easy

- [ ] **Echo Bot** - Create a bot that repeats back any message the user sends.
    - *Concepts:* Basic bot setup, `MessageHandler`, `filters.TEXT`

- [ ] **Welcome Bot** - Build a bot that sends a welcome message with `/start` and shows help with `/help`.
    - *Concepts:* `CommandHandler`, formatted messages (Markdown/HTML)

- [ ] **Inline Calculator** - Simple calculator using inline keyboard buttons.
    - *Concepts:* `InlineKeyboardMarkup`, `CallbackQueryHandler`, `edit_message_text()`

## Medium

- [ ] **Random Quote Bot** - Bot that sends random quotes or jokes on demand using `/quote` or `/joke`.
    - *Concepts:* External API integration with `aiohttp`, error handling

- [ ] **PEMDAS Calculator** - Accepts math expressions and returns results. Example: `/calc 5 + 3`.
    - *Concepts:* Command argument parsing (`context.args`), safe expression evaluation
    - *Note:* Using `eval()` is insecure

- [ ] **Reminder Bot** - Set reminders that message users after a specified time.
    - *Concepts:* `JobQueue`, scheduling one-time jobs, canceling jobs

- [ ] **To-Do List Bot** - Personal task manager with `/add`, `/list`, `/done`, `/clear` commands.
    - *Concepts:* `context.user_data` for persistence, state management per user

- [ ] **Multi-Step Registration Form** - Collect user info (name, email, age) step-by-step.
    - *Concepts:* `ConversationHandler` with states, `entry_points`, `fallbacks`, timeout handling

## Hard

- [ ] **Image Processing Bot** - Accepts images and applies filters (grayscale, blur, resize).
    - *Concepts:* Media handling, `PhotoSize`, Pillow library, sending processed images

- [ ] **Group Management Bot** - Welcome new members, kick spammers, set rules, moderate content.
    - *Concepts:* Chat types, `ChatMemberHandler`, permissions, `restrict_chat_member()`

- [ ] **AI Chatbot Integration** - Integrates with OpenAI API for natural conversations.
    - *Concepts:* Async API calls, conversation context management, streaming responses

- [ ] **Nested Menu Navigation** - Product catalog with categories → subcategories → items.
    - *Concepts:* Nested `ConversationHandler`, regex patterns in callbacks, back/forward navigation

## Capstone Projects

- [ ] **Study Flashcard Bot** - Users create decks, quiz themselves with spaced repetition.
    - *Combines:* ConversationHandler, InlineKeyboards, Database, scheduling

- [ ] **Expense Tracker Bot** - Log expenses, generate reports, send charts.
    - *Combines:* Commands, ConversationHandler, Database (SQLite), matplotlib charts

## General Assignment

- [ ] **URL Downloader** - Accepts links for YouTube, X (Twitter), Instagram. Asks for quality, sends media file.
    - *Concepts:* External libraries (yt-dlp), file handling, progress updates, quality selection menus

## Handler Types Reference

| Handler                | Use Case                          |
|------------------------|-----------------------------------|
| `CommandHandler`       | `/start`, `/help` commands        |
| `MessageHandler`       | Text, photos, documents, stickers |
| `CallbackQueryHandler` | Inline keyboard button presses    |
| `ConversationHandler`  | Multi-step dialogues with states  |
| `InlineQueryHandler`   | Inline mode (`@botname query`)    |
| `PollAnswerHandler`    | Poll/quiz responses               |
| `ChatMemberHandler`    | Member join/leave events          |

## Notes

- **Start with python-telegram-bot (PTB):** Most well-documented library
- **Focus on Async:** Ensure to learn `async def` and `await` syntax
- **Read the Docs:** Telegram's API documentation is excellent
- **Progression:** Echo → Commands → Callbacks → ConversationHandler → Groups

## Resources

- [python-telegram-bot GitHub](https://github.com/python-telegram-bot/python-telegram-bot)
- [Official Examples](https://docs.python-telegram-bot.org/en/stable/examples.html)
- [Handler Types Wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Types-of-Handlers)
- [Telegram Bot Tutorial](https://core.telegram.org/bots/tutorial)
