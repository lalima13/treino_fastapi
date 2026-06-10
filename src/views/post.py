from pydantic import AwareDatetime, BaseModel

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: AwareDatetime | None
