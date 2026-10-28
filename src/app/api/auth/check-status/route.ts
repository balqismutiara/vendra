import { NextRequest, NextResponse } from 'next/server'
import { prisma } from '@/lib/prisma'
import { ApprovalStatus } from '@prisma/client'

export async function POST(request: NextRequest) {
  try {
    const { email } = await request.json()

    if (!email) {
      return NextResponse.json({ error: 'Email required' }, { status: 400 })
    }

    // Check user status
    const user = await prisma.user.findUnique({
      where: { email },
      select: {
        status: true,
        isActive: true,
        company: {
          select: {
            isActive: true
          }
        }
      }
    })

    if (!user) {
      // User not found - don't reveal this for security
      return NextResponse.json({ isBanned: false })
    }

    // Check if banned (REJECTED status or inactive)
    const isBanned = user.status === ApprovalStatus.REJECTED || 
                     !user.isActive || 
                     (user.company && !user.company.isActive)

    return NextResponse.json({ isBanned })

  } catch (error) {
    console.error('Error checking user status:', error)
    return NextResponse.json({ isBanned: false })
  }
}
