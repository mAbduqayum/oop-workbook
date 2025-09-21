# Claude.md - Python Educational Slides

This directory contains Python educational slides created with Touying (Typst) for teaching students.

## Project Purpose
Creating comprehensive, interactive Python slides for student learning using Touying's powerful presentation features.

## Development Workflow

### Slide Development Process
1. **Plan**: Outline learning objectives and lesson structure
2. **Create**: Build slides with clear examples and explanations
3. **Iterate**: Refine content based on educational effectiveness
4. **Test**: Verify all code examples work correctly

## Touying/Typst Guidelines

Refer to examples in `touying_examples/`:
- `main.typ` - Basic simple theme structure
- `dewdrop.typ` - Professional theme with navigation and metadata
- `complex.typ` - Advanced features with animations, theorems, and diagrams

### Animation Features
- Use `#pause` for progressive content revelation
- Use `#meanwhile` for simultaneous content display
- Use `#uncover("2-")[]` for reserving space
- Use `#only("2-")[]` for not reserving space
- Use `#alternatives[][]` for choosing between options

### Educational Content Standards
- Start with simple concepts, build complexity gradually
- Include working code examples that students can run
- Add visual diagrams where helpful
- Use consistent formatting for code blocks
- Include exercises and practice problems

## Development Commands

### Typst/Touying Commands
```bash
# Compile slides
typst compile slides.typ

# Watch for changes during development
typst watch slides.typ

# Compile specific lesson
typst compile lessons/variables.typ
```


## Content Organization

### Lesson Structure
1. **Title slide**: Course/lesson title and metadata
2. **Outline slide**: Lesson overview
3. **Introduction slides**: Topic overview and learning objectives
4. **Concept slides**: Core concepts with explanations
5. **Example slides**: Working code demonstrations
6. **Practice slides**: Student exercises
7. **Summary slides**: Key takeaways

### Advanced Features
Based on `complex.typ` example:
- **Theorems and proofs**: Use `#theorem[]`, `#proof[]`, `#definition[]`
- **Diagrams**: CeTZ for drawings, Fletcher for flowcharts
- **Math equations**: Full LaTeX math support with animations
- **Side-by-side layouts**: `#slide(composer: (1fr, 1fr))[][]`
- **Speaker notes**: `#speaker-note[]`

## Educational Best Practices

### Slide Design
- Use large, readable fonts for code
- Maintain consistent color scheme
- Include slide numbers for easy reference
- Add progress indicators for long lessons

### Content Guidelines
- One concept per slide when possible
- Use analogies and real-world examples
- Include interactive elements with `#pause`
- Provide clear learning objectives
- End lessons with practical exercises

### Student Engagement
- Include "Try this" sections
- Add debugging exercises
- Use progressive disclosure with pauses
- Include visual representations of concepts

## Repository Organization

```
python-syllabus/
├── slides/              # Main slide files
├── examples/            # Code examples from slides
├── exercises/           # Student practice problems
├── assets/              # Images, diagrams
├── touying_examples/    # Touying reference examples
├── touying_themes/      # Custom themes
└── compiled/            # Generated PDF slides
```

## Quality Checklist

Before finalizing slides:
- [ ] All code examples tested and working
- [ ] Consistent formatting throughout
- [ ] Learning objectives clearly stated
- [ ] Progressive difficulty maintained
- [ ] Interactive elements properly placed
- [ ] Slides compile without errors
- [ ] Navigation and metadata properly configured
