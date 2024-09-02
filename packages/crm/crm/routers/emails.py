from fastapi import APIRouter  # type: ignore


router = APIRouter()


@router.get('')
def api_public_emails(db: DbSession, pagination: PaginationParams):  # type: ignore
    raise NotImplementedError

    emails = db.query(Email).order_by(desc(Email.time_scheduled)).all()


@router.post('/<email_id>/approve')
def api_public_email_approve(db: DbSession, email_id: int):  # type: ignore
    raise NotImplementedError

    email = db.get(Email, email_id)

    api_logger.debug(f"approving email {email}")

    email.approved = not email.approved
    db.add(email)
    db.commit()

    return jsonify({
        'status': 'succes',
        'email': email.to_dict()
    })
