"""Reusable UI builder for AutoMate X workspaces."""

from typing import Sequence, Tuple

import customtkinter as ctk


def build_workspace(
    parent: ctk.CTkFrame,
    title: str,
    description: str,
    features: Sequence[Tuple[str, str]],
) -> ctk.CTkFrame:
    """Build a consistent workspace screen with informational feature cards."""

    frame = ctk.CTkScrollableFrame(parent, fg_color="transparent")
    frame.grid_columnconfigure((0, 1), weight=1, uniform="workspace")

    header = ctk.CTkFrame(frame, fg_color="transparent")
    header.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(8, 22))
    header.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(
        header,
        text=title,
        font=ctk.CTkFont(family="Segoe UI", size=27, weight="bold"),
        text_color="#111827",
        anchor="w",
    ).grid(row=0, column=0, sticky="w", pady=(0, 8))

    ctk.CTkLabel(
        header,
        text=description,
        font=ctk.CTkFont(family="Segoe UI", size=13),
        text_color="#6b7280",
        anchor="w",
        justify="left",
        wraplength=850,
    ).grid(row=1, column=0, sticky="w")

    for index, (feature_title, feature_description) in enumerate(features):
        card = ctk.CTkFrame(
            frame,
            fg_color="#ffffff",
            corner_radius=16,
            border_width=1,
            border_color="#e5e7eb",
        )
        row, column = divmod(index, 2)
        card.grid(
            row=row + 1,
            column=column,
            sticky="nsew",
            padx=(0, 10) if column == 0 else (10, 0),
            pady=10,
        )

        ctk.CTkLabel(
            card,
            text=feature_title,
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color="#111827",
            anchor="w",
        ).pack(fill="x", padx=18, pady=(18, 8))

        ctk.CTkLabel(
            card,
            text=feature_description,
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#6b7280",
            anchor="w",
            justify="left",
            wraplength=390,
        ).pack(fill="x", padx=18, pady=(0, 18))

    return frame