import { Injectable } from '@nestjs/common';

@Injectable()
export class NotifyService {
  handleLineEvent(payload: Record<string, unknown>) {
    return { status: 'received', eventType: payload['type'] ?? 'unknown' };
  }
}
