
# 📘 Cybersecurity Notes – Authentication & Access Control
**Date:** July 25, 2025  
**Author:** Nazreen Shanavaz

---

## 🔐 1. Authentication vs Authorization

| Concept         | What it Means                          | Example                                |
|----------------|------------------------------------------|----------------------------------------|
| **Authentication** | Verifying **who you are**              | Logging into an app using your password |
| **Authorization**  | Deciding **what you can access**       | Only admins can delete users           |

---

## 🔑 2. Authentication Methods

- **Something you know:** Password, PIN  
- **Something you have:** OTP, Smart card  
- **Something you are:** Fingerprint, Face ID  

---

## 📚 3. Role-Based Access Control (RBAC)

- Access is based on **user's role**  
- Example:  
  - Student → can view marks  
  - Teacher → can update marks  
- Simple and easy to manage in organizations

---

## 🧬 4. Attribute-Based Access Control (ABAC)

- Access based on **user + resource + environment attributes**  
- Example:  
  - Student AND age > 18 AND access time is 9am–5pm → Access allowed  
- Offers more **flexibility and control** than RBAC

---

## 🎫 5. Web Authentication & Tokens (Microsoft Entra ID)

- Microsoft Entra ID is an **Identity Provider (IdP)**  
- User logs in once → gets a **security token**  
- Token has **claims** (like user ID, roles, expiry)  
- Token is used to access multiple apps → enables **Single Sign-On (SSO)**

---

## 🔐 6. Benefits of Web SSO (Single Sign-On)

- One login = access to multiple apps  
- Reduces password fatigue  
- Improves security (less password reuse)  
- Managed centrally via Entra ID

---

## 💡 Summary

Today I learned about how **authentication**, **access control**, and **SSO** work in real-world systems like Microsoft Entra. I also understood the difference between **RBAC** and **ABAC**, which are two common ways to control access in secure systems.
