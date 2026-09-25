# Time Value Decision

Cross-platform Agent Skill for Codex, Claude Code, and Gemini CLI. It fact-checks options, calculates money-versus-time trade-offs, and challenges whether paying more is actually worth it.

Agent Skill สำหรับ Codex, Claude Code และ Gemini CLI เพื่อช่วยตัดสินใจเมื่อต้องแลกเงินกับเวลา ความสะดวก พลังงาน หรือความแน่นอน

เหมาะกับการเปรียบเทียบเที่ยวบิน โรงแรม การเดินทาง ค่าส่ง Subscription การจ้างคนทำงานแทน และการอัปเกรดต่าง ๆ

Skill นี้ไม่กำหนดว่าเวลาของทุกคนต้องมีราคาเท่าไร และไม่ตัดสินใจแทนผู้ใช้ แต่ช่วยให้เห็นสมมติฐาน จุดคุ้มทุน ความเสี่ยง และเหตุผลที่อาจทำให้คำตอบเปลี่ยน

## ความสามารถ

- **Compare** คำนวณ Effective Cost, Break-even Value of Time และ Sensitivity
- **Fact Check** ค้นและตรวจสอบข้อมูลปัจจุบันก่อนนำมาคำนวณ
- **Grill Me** ถามกลับเพื่อทดสอบว่าเราต้องการสิ่งนั้นจริง หรือกำลังหาเหตุผลรองรับความอยาก

## รองรับ

| Agent | รูปแบบ Skill | เรียกใช้ |
| --- | --- | --- |
| Codex | `SKILL.md` | `$time-value-decision` หรือพิมพ์คำขอที่ตรงกับ Skill |
| Claude Code | `SKILL.md` | `/time-value-decision` หรือพิมพ์คำขอที่ตรงกับ Skill |
| Gemini CLI | `SKILL.md` | พิมพ์คำขอที่ตรงกับ Skill แล้วอนุมัติการ Activate |

Skill หลักใช้ไฟล์ชุดเดียวกันทั้งสามแพลตฟอร์ม ส่วน `agents/openai.yaml` เป็น metadata เพิ่มเติมสำหรับ Codex และไม่กระทบ Claude Code หรือ Gemini CLI

## ติดตั้ง

### Codex

ติดตั้งแบบ Personal Skill:

```bash
git clone https://github.com/trrekiiz/time-value-decision.git ~/.codex/skills/time-value-decision
```

จากนั้นเปิด Codex ใหม่

### Claude Code

ติดตั้งแบบ Personal Skill:

```bash
git clone https://github.com/trrekiiz/time-value-decision.git ~/.claude/skills/time-value-decision
```

จากนั้นเปิด Claude Code ใหม่ หรือเริ่ม session ใหม่

### Gemini CLI

ติดตั้งจาก GitHub โดยตรง:

```bash
gemini skills install https://github.com/trrekiiz/time-value-decision
```

ตรวจสอบด้วย `gemini skills list` และใช้ `/skills reload` หาก session เดิมยังไม่เห็น Skill

### ดาวน์โหลด ZIP

1. ดาวน์โหลด repository เป็น ZIP
2. แตกโฟลเดอร์และเปลี่ยนชื่อเป็น `time-value-decision`
3. วางไว้ในโฟลเดอร์ Skill ของ Agent ที่ใช้
   - Codex: `~/.codex/skills/time-value-decision`
   - Claude Code: `~/.claude/skills/time-value-decision`
   - Gemini CLI: `~/.gemini/skills/time-value-decision`
4. เปิด Agent ใหม่หรือ reload รายการ Skills

## ตัวอย่างการใช้งาน

```text
ใช้ time-value-decision เปรียบเทียบเที่ยวบินสองตัวเลือกนี้
ตรวจสอบเวลาเดินทางจริง คำนวณ break-even และ Grill me
ว่าฉันต้องการจ่ายเพิ่มเพื่อบินตรงจริงหรือเปล่า
```

```text
ใช้ time-value-decision เปรียบเทียบโรงแรม A กับ B
แสดงเวลาที่ใช้เพิ่มทั้งหมด จุดคุ้มทุน และ sensitivity
ที่ 200, 400, 600 และ 1,000 บาทต่อชั่วโมง
```

## หลักคิดสำคัญ

- Value of Time ไม่เท่ากับเงินเดือนต่อชั่วโมงโดยอัตโนมัติ
- เวลาที่ประหยัดได้ต้องเป็นเวลาที่ใช้ประโยชน์ได้จริง
- Friction และ Risk ควรแสดงให้เห็น แม้ยังตีราคาเป็นเงินไม่ได้
- เราไม่จำเป็นต้อง optimize ทุกนาที เพราะบางกิจกรรมมีคุณค่าในตัวเอง
- AI ช่วยค้นข้อมูลและคำนวณ ส่วนผู้ใช้ยังเป็นคนกำหนดคุณค่าและตัดสินใจ

## โครงสร้าง

```text
time-value-decision/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── calculator.md
│   ├── fact-check.md
│   └── grill-me.md
└── scripts/
    └── compare_options.py
```

## Disclaimer

ผลลัพธ์เป็นเครื่องมือช่วยคิด ไม่ใช่คำแนะนำทางการเงิน กฎหมาย หรือความปลอดภัยในการเดินทาง ข้อมูลที่เปลี่ยนตามเวลา เช่น ราคา ตารางบิน และเงื่อนไขผู้ให้บริการ ควรตรวจสอบจากแหล่งข้อมูลปัจจุบันก่อนตัดสินใจ
