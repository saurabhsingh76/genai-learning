# LangChain Structured Output

Document to understanding and implementing structured output in LangChain for building production-ready AI applications that integrate with databases, APIs, and other systems.

## Table of Contents

1. [Introduction to Structured Output](#introduction-to-structured-output)
2. [Why Structured Output is Essential](#why-structured-output-is-essential)
3. [Real-World Use Cases](#real-world-use-cases)
4. [Approaches to Structured Output](#approaches-to-structured-output)
5. [The `with_structured_output` Function](#the-with_structured_output-function)
6. [Schema Definition Methods](#schema-definition-methods)
   - [TypedDict](#typeddict)
   - [Pydantic](#pydantic)
   - [JSON Schema](#json-schema)
7. [When to Use Which Method](#when-to-use-which-method)
8. [Important Implementation Details](#important-implementation-details)
9. [Best Practices](#best-practices)

## Introduction to Structured Output

### What is Structured vs Unstructured Output?

**Unstructured Output (Traditional LLM Response):**
- Raw text responses from LLMs (e.g., "New Delhi is the capital of India")
- Human-readable but difficult for systems to process programmatically
- No predefined format or data structure
- Requires manual parsing and interpretation

**Structured Output (Enhanced LLM Response):**
- Responses in well-defined data formats like JSON, XML, or custom schemas
- Machine-readable and easily parsable by other systems
- Follows a consistent, predefined structure
- Enables seamless integration with databases, APIs, and other applications

### The Core Problem

Traditional LLMs excel at human-to-human communication but struggle with machine-to-machine interaction. The unstructured nature of text responses creates barriers when trying to:
- Store responses in databases
- Pass data to APIs
- Integrate with existing software systems
- Build automated workflows

### The Solution

Structured output transforms LLM responses from free-form text into standardized data formats, enabling:
- **System Integration**: Connect LLMs with databases, APIs, and other services
- **Automated Processing**: Process responses programmatically without manual parsing
- **Data Consistency**: Ensure predictable output formats across different queries
- **Production Scalability**: Build reliable, production-ready AI applications

## Why Structured Output is Essential

### Enabling Machine-to-Machine Communication

Structured output serves as a bridge between human language understanding (LLMs) and system processing requirements. This enables:

1. **Database Integration**: Store extracted information directly in structured database tables
2. **API Development**: Create reliable APIs that return consistent, parseable data
3. **Workflow Automation**: Chain multiple systems together seamlessly
4. **Agent Development**: Enable AI agents to interact with tools and services

### Key Benefits

- **Consistency**: Same input types always produce predictable output formats
- **Reliability**: Reduces errors from manual parsing of text responses
- **Scalability**: Handles large volumes of data processing automatically
- **Integration**: Works seamlessly with existing software infrastructure
- **Maintainability**: Easier to update and modify system behavior

## Real-World Use Cases

### 1. Data Extraction Systems

**Scenario**: Building a job portal like Naukri.com
**Problem**: Extract structured information from uploaded resumes
**Solution**: 
- Upload resume → Extract text → Send to LLM → Receive structured data
- Extract: Name, last company, education marks, skills, experience
- Store directly in database tables for search and filtering

**Benefits**:
- Automated resume processing
- Consistent data storage
- Easy search and filtering capabilities
- Reduced manual data entry

### 2. API Development for Content Analysis

**Scenario**: Amazon product review analysis system
**Problem**: Long, unstructured reviews need structured analysis
**Solution**:
- Input: Raw product review text
- Output: Structured analysis containing:
  - Key topics discussed (battery, display, processor)
  - Pros and cons lists
  - Overall sentiment
  - Review summary
- Expose via API for other services to consume

**Benefits**:
- Automated review analysis
- Standardized review insights
- API-driven architecture
- Multi-language support potential

### 3. Agent Development

**Scenario**: Building AI agents with tool capabilities
**Problem**: Agents need structured data to interact with tools
**Example**: Math agent with calculator tool
- User query: "Find the square root of 2"
- Agent needs to extract: Operation (square root) + Number (2)
- Pass structured data to calculator tool
- Return processed result

**Benefits**:
- Tool integration capabilities
- Complex workflow automation
- Multi-step reasoning support
- Enhanced agent functionality

## Approaches to Structured Output

LangChain provides two main approaches based on LLM capabilities:

### 1. LLMs with Native Structured Output Support

**Compatible Models**: OpenAI GPT models, Claude, other trained models
**Method**: Use `with_structured_output` function
**Advantage**: Built-in support, more reliable, better performance

### 2. LLMs without Native Support

**Compatible Models**: Older open-source models, custom fine-tuned models
**Method**: Use Output Parsers (covered in next video/guide)
**Advantage**: Works with any LLM, more universal compatibility

**Note**: This guide focuses on the first approach using `with_structured_output`.

## The `with_structured_output` Function

### How It Works

The `with_structured_output` function simplifies structured output generation by:

1. **Schema Definition**: You define the desired output structure
2. **Automatic Prompt Generation**: Creates system prompts behind the scenes
3. **Response Processing**: Converts LLM output to structured format
4. **Type Safety**: Ensures output matches defined schema

### Basic Workflow

```
Traditional Flow:
model.invoke(prompt) → text response

Structured Flow:
model.with_structured_output(schema) → structured_model
structured_model.invoke(prompt) → structured response
```

### Behind the Scenes

When you use `with_structured_output`, LangChain:
1. Generates a system prompt describing the desired output format
2. Includes your schema specifications in the prompt
3. Instructs the LLM to return responses in JSON format
4. Parses and validates the response against your schema

Example generated system prompt:
```
"You are an AI assistant that extracts structured insights from text. 
Given a product review, extract:
- summary: A brief overview of the main points
- sentiment: Overall tone (positive, negative, neutral)
Return the response in JSON format."
```

## Schema Definition Methods

### TypedDict

#### What is TypedDict?

TypedDict is a Python feature for defining dictionary structures with type hints. It specifies what keys should exist and their expected data types, improving code readability and IDE support.

#### Key Features

1. **Type Hinting**: Provides clear documentation of expected data structure
2. **IDE Support**: Enables autocomplete and type checking in development
3. **Static Analysis**: Compatible with tools like mypy for type validation
4. **Zero Runtime Cost**: No performance overhead during execution

#### Basic Implementation

**Simple Schema**:
```python
class Review(TypedDict):
    summary: str
    sentiment: str
```

**Complex Schema with Advanced Features**:
```python
class DetailedReview(TypedDict):
    key_themes: List[str]  # Multiple values in a list
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["positive", "negative", "neutral"], "Overall review sentiment"]
    pros: Optional[List[str]]  # Optional field
    cons: Optional[List[str]]  # Optional field
    reviewer_name: Optional[str]  # May not always be present
```

#### Advanced Features

**Annotations**: Add descriptions to guide LLM understanding
```python
summary: Annotated[str, "A brief summary highlighting key points"]
```

**Optional Fields**: Handle fields that may not always be present
```python
pros: Optional[List[str]]  # Will be None if not found
```

**Literal Values**: Restrict responses to specific options
```python
sentiment: Literal["positive", "negative", "neutral"]
```

**List Types**: Handle multiple values
```python
key_themes: List[str]  # Array of strings
```

#### Limitations

- **No Runtime Validation**: Type hints don't enforce data types at runtime
- **LLM Dependency**: Relies on LLM to follow schema correctly
- **Error Handling**: Limited options for handling schema violations

### Pydantic

#### What is Pydantic?

Pydantic is a powerful data validation and parsing library for Python that provides robust schema definition with automatic validation, type coercion, and error handling.

#### Key Advantages Over TypedDict

1. **Runtime Validation**: Enforces data types and raises errors for violations
2. **Type Coercion**: Automatically converts compatible types (e.g., "32" string to 32 integer)
3. **Built-in Validators**: Email validation, URL validation, etc.
4. **Custom Constraints**: Range validation, pattern matching, custom rules
5. **Rich Error Messages**: Detailed error information for debugging
6. **Default Values**: Built-in support for default field values

#### Basic Implementation

**Simple Model**:
```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
```

**Advanced Model with Validation**:
```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class ReviewAnalysis(BaseModel):
    summary: str = Field(description="A brief summary of the review")
    sentiment: str = Field(description="Sentiment: positive, negative, or neutral")
    key_themes: List[str] = Field(description="Main topics discussed")
    pros: Optional[List[str]] = Field(default=None, description="Positive aspects mentioned")
    cons: Optional[List[str]] = Field(default=None, description="Negative aspects mentioned")
    rating_score: float = Field(gt=0, le=10, description="Numeric rating between 0-10")
    reviewer_email: Optional[EmailStr] = Field(default=None)
```

#### Advanced Features

**Field Constraints**:
```python
cgpa: float = Field(gt=0, le=10)  # Must be between 0 and 10
age: int = Field(ge=18, le=100)   # Age between 18-100
```

**Default Values**:
```python
status: str = Field(default="pending")
created_at: datetime = Field(default_factory=datetime.now)
```

**Built-in Validators**:
```python
email: EmailStr  # Automatic email validation
website: HttpUrl  # URL validation
```

**Custom Descriptions**:
```python
score: float = Field(description="Performance score from 0.0 to 1.0")
```

#### Data Conversion

Pydantic objects can be converted to different formats:

**To Dictionary**:
```python
review_dict = review_object.model_dump()
```

**To JSON**:
```python
review_json = review_object.model_dump_json()
```

#### Error Handling

Pydantic provides detailed validation errors:
```python
ValidationError: 1 validation error for Student
age
  Input should be a valid integer [type=int_parsing, input_value='not_a_number']
```

### JSON Schema

#### What is JSON Schema?

JSON Schema is a vocabulary that allows you to annotate and validate JSON documents. It's language-agnostic and widely supported across different programming languages.

#### Use Cases

1. **Multi-language Projects**: Share schemas between Python backend and JavaScript frontend
2. **API Documentation**: Standardize data formats across different services
3. **Universal Compatibility**: Works with any system that supports JSON
4. **Legacy Integration**: Integrate with existing systems using JSON

#### Basic Structure

```python
review_schema = {
    "title": "ReviewAnalysis",
    "description": "Structured analysis of product reviews",
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "Brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "Overall sentiment"
        },
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Main topics discussed"
        },
        "rating": {
            "type": "number",
            "minimum": 1,
            "maximum": 5,
            "description": "Numeric rating"
        }
    },
    "required": ["summary", "sentiment"]
}
```

#### Advanced Features

**Data Type Validation**:
- `"type": "string"` - Text values
- `"type": "integer"` - Whole numbers
- `"type": "number"` - Decimal numbers
- `"type": "boolean"` - True/false values
- `"type": "array"` - Lists of values
- `"type": "object"` - Nested objects

**Constraints**:
- `"minimum"`, `"maximum"` - Numeric ranges
- `"enum"` - Restricted value lists
- `"minLength"`, `"maxLength"` - String length limits
- `"pattern"` - Regular expression matching

**Required Fields**:
```python
"required": ["summary", "sentiment", "rating"]
```

#### Output Format

When using JSON Schema with `with_structured_output`, the output is a Python dictionary matching the schema structure.

## When to Use Which Method

### TypedDict - Choose When:

**Best For:**
- Python-only projects
- Simple schema requirements
- Type hinting and IDE support priority
- No strict validation requirements
- Quick prototyping and development

**Advantages:**
- Minimal setup and dependencies
- Native Python support
- Good IDE integration
- Fast development cycle

**Limitations:**
- No runtime validation
- Limited error handling
- Python-specific

### Pydantic - Choose When:

**Best For:**
- Production applications
- Data validation requirements
- Complex schema with constraints
- Error handling importance
- Type coercion needs

**Advantages:**
- Robust validation system
- Excellent error messages
- Type coercion capabilities
- Rich ecosystem support
- Popular in Python community

**Use Cases:**
- API development (FastAPI)
- Data processing pipelines
- User input validation
- Complex business logic

### JSON Schema - Choose When:

**Best For:**
- Multi-language environments
- API documentation needs
- Legacy system integration
- Universal schema sharing
- Cross-platform compatibility

**Advantages:**
- Language agnostic
- Industry standard
- Wide tool support
- Documentation generation

**Use Cases:**
- Microservices architecture
- API specification
- Data exchange formats
- Cross-team collaboration

## Important Implementation Details

### Method Parameter in `with_structured_output`

The `method` parameter controls how structured output is generated:

#### `json_mode`
**When to Use:**
- General data extraction tasks
- Claude or Gemini models
- Simple structured responses
- JSON-focused applications

**Characteristics:**
- Focuses on JSON format generation
- Better for data extraction use cases
- Recommended for most LLMs except OpenAI

#### `function_calling`  
**When to Use:**
- OpenAI models (often default)
- Agent development with tools
- Function/tool integration scenarios
- Complex reasoning tasks

**Characteristics:**
- Leverages function calling capabilities
- Better for agent-tool interactions
- More structured reasoning process

### LLM Compatibility

**Models Supporting Structured Output:**
- OpenAI GPT-3.5, GPT-4 series
- Anthropic Claude models
- Google Gemini models  
- Most modern commercial LLMs

**Models Requiring Output Parsers:**
- Older open-source models
- Fine-tuned models without structured training
- Smaller models like TinyLlama
- Custom-trained models

**Testing Compatibility:**
If `with_structured_output` doesn't work with your model, use Output Parsers (covered in the next guide) as an alternative approach.

## Best Practices

### Schema Design

**Keep Schemas Simple:**
- Start with basic fields and add complexity gradually
- Use clear, descriptive field names
- Avoid deeply nested structures initially

**Use Descriptive Annotations:**
- Always add descriptions to fields
- Provide examples in descriptions when helpful
- Be explicit about expected formats

**Handle Optional Data:**
- Use `Optional` for fields that might not be present
- Provide sensible defaults where appropriate
- Document when fields are conditional

### Error Handling

**Validate Responses:**
- Always validate structured output before using
- Implement fallback mechanisms for validation failures
- Log validation errors for debugging

**Test Edge Cases:**
- Test with incomplete input data
- Verify behavior with unexpected input formats
- Test schema constraints thoroughly

### Performance Optimization

**Choose Appropriate Schemas:**
- Use TypedDict for simple, fast operations
- Use Pydantic when validation is critical
- Use JSON Schema for cross-language compatibility

**Cache Schema Definitions:**
- Reuse schema definitions across requests
- Avoid recreating schemas repeatedly
- Consider schema versioning for production systems

### Development Workflow

**Start Simple:**
- Begin with basic TypedDict schemas
- Add validation with Pydantic as needed
- Consider JSON Schema for complex projects

**Iterative Improvement:**
- Test schemas with real data
- Refine based on LLM responses
- Monitor and adjust constraint parameters

**Documentation:**
- Document schema purposes and use cases
- Maintain examples of expected inputs/outputs
- Version schemas for backward compatibility

### Integration Patterns

**Database Integration:**
- Map schema fields to database columns
- Use consistent naming conventions
- Plan for schema evolution

**API Development:**
- Align schemas with API response formats
- Use consistent error handling
- Implement proper status codes

**Agent Development:**
- Design schemas for tool compatibility
- Include metadata for agent decision-making
- Plan for multi-step workflows

## Conclusion

Structured output is a fundamental capability that transforms LLMs from simple chat interfaces into powerful system integration tools. By providing structured, parseable responses, LLMs can seamlessly integrate with databases, APIs, and other software systems, enabling the development of sophisticated AI-powered applications.

**Key Takeaways:**

1. **Structured output enables system integration** - Connect LLMs with databases, APIs, and other services
2. **Choose the right schema method** - TypedDict for simplicity, Pydantic for validation, JSON Schema for universality  
3. **Design schemas thoughtfully** - Start simple, add descriptions, handle optional fields
4. **Validate and test thoroughly** - Ensure reliability in production environments
5. **Consider compatibility** - Not all LLMs support structured output natively


The power of structured output lies in its ability to bridge the gap between human language understanding and machine processing requirements, making it an essential tool for building production-ready AI applications.
