from datetime import datetime

import pytest
from file_upload import FileUpload
from pydantic import ValidationError


def test_file_upload_basic():
    upload = FileUpload(
        filename="document.pdf",
        size_bytes=1048576,
        mime_type="application/pdf",
        upload_date=datetime(2024, 1, 15, 10, 30, 0),
    )
    assert upload.filename == "document.pdf"
    assert upload.size_bytes == 1048576
    assert upload.mime_type == "application/pdf"
    assert upload.upload_date == datetime(2024, 1, 15, 10, 30, 0)


def test_file_extension_pdf():
    upload = FileUpload(
        filename="document.pdf",
        size_bytes=1048576,
        mime_type="application/pdf",
        upload_date=datetime(2024, 1, 15, 10, 30, 0),
    )
    assert upload.file_extension == "pdf"


def test_file_extension_jpg():
    upload = FileUpload(
        filename="photo.jpg",
        size_bytes=2097152,
        mime_type="image/jpeg",
        upload_date=datetime(2024, 1, 15, 11, 0, 0),
    )
    assert upload.file_extension == "jpg"


def test_size_mb_one_megabyte():
    upload = FileUpload(
        filename="document.pdf",
        size_bytes=1048576,
        mime_type="application/pdf",
        upload_date=datetime(2024, 1, 15, 10, 30, 0),
    )
    assert upload.size_mb == 1.0


def test_size_mb_two_megabytes():
    upload = FileUpload(
        filename="photo.jpg",
        size_bytes=2097152,
        mime_type="image/jpeg",
        upload_date=datetime(2024, 1, 15, 11, 0, 0),
    )
    assert upload.size_mb == 2.0


def test_size_mb_half_megabyte():
    upload = FileUpload(
        filename="small.txt",
        size_bytes=524288,
        mime_type="text/plain",
        upload_date=datetime(2024, 1, 15, 11, 0, 0),
    )
    assert upload.size_mb == 0.5


def test_mime_type_jpeg():
    upload = FileUpload(
        filename="photo.jpg",
        size_bytes=1024,
        mime_type="image/jpeg",
        upload_date=datetime.now(),
    )
    assert upload.mime_type == "image/jpeg"


def test_mime_type_png():
    upload = FileUpload(
        filename="photo.png",
        size_bytes=1024,
        mime_type="image/png",
        upload_date=datetime.now(),
    )
    assert upload.mime_type == "image/png"


def test_mime_type_gif():
    upload = FileUpload(
        filename="animation.gif",
        size_bytes=1024,
        mime_type="image/gif",
        upload_date=datetime.now(),
    )
    assert upload.mime_type == "image/gif"


def test_mime_type_text():
    upload = FileUpload(
        filename="document.txt",
        size_bytes=1024,
        mime_type="text/plain",
        upload_date=datetime.now(),
    )
    assert upload.mime_type == "text/plain"


def test_file_too_large():
    with pytest.raises(ValidationError):
        FileUpload(
            filename="huge.pdf",
            size_bytes=20000000,
            mime_type="application/pdf",
            upload_date=datetime.now(),
        )


def test_file_size_exactly_10mb():
    upload = FileUpload(
        filename="large.pdf",
        size_bytes=10485760,
        mime_type="application/pdf",
        upload_date=datetime.now(),
    )
    assert upload.size_bytes == 10485760
    assert upload.size_mb == 10.0


def test_file_size_exceeds_10mb():
    with pytest.raises(ValidationError):
        FileUpload(
            filename="huge.pdf",
            size_bytes=10485761,
            mime_type="application/pdf",
            upload_date=datetime.now(),
        )


def test_invalid_mime_type():
    with pytest.raises(ValidationError):
        FileUpload(
            filename="file.exe",
            size_bytes=1024,
            mime_type="application/x-msdownload",
            upload_date=datetime.now(),
        )


def test_filename_no_extension():
    with pytest.raises(ValidationError):
        FileUpload(
            filename="noextension",
            size_bytes=1024,
            mime_type="text/plain",
            upload_date=datetime.now(),
        )


def test_filename_multiple_dots():
    upload = FileUpload(
        filename="my.document.pdf",
        size_bytes=1024,
        mime_type="application/pdf",
        upload_date=datetime.now(),
    )
    assert upload.file_extension == "pdf"


def test_empty_filename():
    with pytest.raises(ValidationError):
        FileUpload(
            filename="",
            size_bytes=1024,
            mime_type="text/plain",
            upload_date=datetime.now(),
        )


def test_filename_too_long():
    with pytest.raises(ValidationError):
        FileUpload(
            filename="x" * 256 + ".txt",
            size_bytes=1024,
            mime_type="text/plain",
            upload_date=datetime.now(),
        )


def test_zero_size():
    with pytest.raises(ValidationError):
        FileUpload(
            filename="empty.txt",
            size_bytes=0,
            mime_type="text/plain",
            upload_date=datetime.now(),
        )


def test_negative_size():
    with pytest.raises(ValidationError):
        FileUpload(
            filename="invalid.txt",
            size_bytes=-1024,
            mime_type="text/plain",
            upload_date=datetime.now(),
        )


def test_serialization():
    upload = FileUpload(
        filename="document.pdf",
        size_bytes=1048576,
        mime_type="application/pdf",
        upload_date=datetime(2024, 1, 15, 10, 30, 0),
    )
    data = upload.model_dump()
    assert data["filename"] == "document.pdf"
    assert data["size_bytes"] == 1048576
    assert data["mime_type"] == "application/pdf"
    assert data["upload_date"] == datetime(2024, 1, 15, 10, 30, 0)
